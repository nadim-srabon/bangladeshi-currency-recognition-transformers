# api/main.py
# Run with: uvicorn api.main:app --reload
# POST /predict with a currency note image → get denomination + confidence

import io
import json
import numpy as np
from PIL import Image
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import onnxruntime as ort
from scipy.special import softmax

# ── Load metadata & model at startup ──────────────────────────────
BASE = Path(__file__).parent.parent / "model_export"

with open(BASE / "model_metadata.json") as f:
    META = json.load(f)

MODEL_FILE = next(BASE.glob("*.onnx"))
SESSION    = ort.InferenceSession(
    str(MODEL_FILE),
    providers=["CUDAExecutionProvider", "CPUExecutionProvider"]
)

IMG_SIZE       = META["img_size"]
CLASS_NAMES    = META["class_names"]
IMAGENET_MEAN  = np.array(META["imagenet_mean"], dtype=np.float32)
IMAGENET_STD   = np.array(META["imagenet_std"],  dtype=np.float32)

# ── App ────────────────────────────────────────────────────────────
app = FastAPI(
    title="Bangladeshi Currency Recognition API",
    description="Classifies Bangladeshi Taka banknote denominations using Vision Transformers.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)


def preprocess(image_bytes: bytes) -> np.ndarray:
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE), Image.BILINEAR)
    arr = np.array(img, dtype=np.float32) / 255.0
    arr = (arr - IMAGENET_MEAN) / IMAGENET_STD
    return arr.transpose(2, 0, 1)[None]  # (1, 3, H, W)


@app.get("/")
def root():
    return {"message": "Bangladeshi Currency Recognition API",
            "classes": CLASS_NAMES,
            "model":   META["model_name"],
            "accuracy": f"{META['accuracy']:.2f}%"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "File must be an image.")

    raw     = await file.read()
    x       = preprocess(raw)
    logits  = SESSION.run(None, {"image": x})[0][0]
    probs   = softmax(logits)

    top3_idx  = probs.argsort()[::-1][:3]
    top3      = [{"denomination": f"{CLASS_NAMES[i]} TK",
                  "confidence": round(float(probs[i]) * 100, 2)}
                 for i in top3_idx]

    return {
        "prediction":  f"{CLASS_NAMES[top3_idx[0]]} TK",
        "confidence":  round(float(probs[top3_idx[0]]) * 100, 2),
        "top3":        top3,
    }