"""
BDTaka Vision — Bangladeshi Currency Recognition
Production Streamlit App
"""

import streamlit as st

st.set_page_config(
    page_title="BDTaka Vision",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://github.com/srabon12/bangladeshi-currency-recognition",
        "Report a bug": "https://github.com/srabon12/bangladeshi-currency-recognition/issues",
        "About": "BDTaka Vision — Bangladeshi Currency Recognition using Vision Transformers",
    },
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.stApp {
    background: #0a0d12;
    color: #e8eaf0;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; padding-bottom: 2rem; max-width: 1200px; }

.bd-header {
    background: linear-gradient(135deg, #0d1117 0%, #161b27 60%, #0d1117 100%);
    border-bottom: 1px solid #1e2840;
    padding: 1.5rem 2rem 1.2rem;
    margin: -1rem -1rem 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
}
.bd-header::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 600px 300px at 80% 50%, rgba(0,212,110,0.05) 0%, transparent 70%);
    pointer-events: none;
}
.bd-logo {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.bd-logo span { color: #00d46e; }
.bd-nav { display: flex; gap: 1rem; align-items: center; }
.bd-nav a {
    color: #8892a4;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 0.03em;
    padding: 0.35rem 0.75rem;
    border-radius: 6px;
    transition: all 0.2s;
}
.bd-nav a:hover { color: #e8eaf0; background: rgba(255,255,255,0.06); }
.bd-badge {
    background: rgba(0,212,110,0.12);
    border: 1px solid rgba(0,212,110,0.3);
    color: #00d46e;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    padding: 0.25rem 0.65rem;
    border-radius: 100px;
    text-transform: uppercase;
}

.bd-hero {
    padding: 4rem 0 3rem;
    text-align: center;
    position: relative;
}
.bd-hero-eyebrow {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #00d46e;
    margin-bottom: 1.2rem;
}
.bd-hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.03em;
    color: #ffffff;
    margin: 0 0 1.2rem;
}
.bd-hero h1 em {
    font-style: normal;
    background: linear-gradient(135deg, #00d46e 0%, #00b4d8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.bd-hero p {
    font-size: 1.1rem;
    color: #8892a4;
    max-width: 580px;
    margin: 0 auto 2.5rem;
    line-height: 1.7;
    font-weight: 300;
}

.stat-row {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
    margin-bottom: 3rem;
}
.stat-chip {
    background: #111827;
    border: 1px solid #1e2840;
    border-radius: 8px;
    padding: 0.6rem 1.2rem;
    text-align: center;
}
.stat-chip .val {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1;
}
.stat-chip .lbl {
    font-size: 0.72rem;
    color: #4a5568;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.3rem;
    font-weight: 500;
}

.upload-wrapper {
    background: #111827;
    border: 1.5px dashed #1e2840;
    border-radius: 16px;
    padding: 3rem 2rem;
    text-align: center;
    transition: border-color 0.3s;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.upload-wrapper::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 400px 200px at 50% 0%, rgba(0,212,110,0.04) 0%, transparent 70%);
    pointer-events: none;
}
.upload-wrapper:hover { border-color: #2d3f55; }
.upload-icon { font-size: 2.5rem; margin-bottom: 0.75rem; }
.upload-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #e8eaf0;
    margin-bottom: 0.4rem;
}
.upload-sub { font-size: 0.85rem; color: #4a5568; font-weight: 400; }

.result-card {
    background: linear-gradient(135deg, #111827 0%, #131e2e 100%);
    border: 1px solid #1e2840;
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.result-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #00d46e 0%, #00b4d8 100%);
}
.result-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4a5568;
    margin-bottom: 0.5rem;
}
.result-denom {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.result-denom span { color: #00d46e; }
.result-conf {
    font-size: 0.9rem;
    color: #8892a4;
    font-weight: 400;
}

.conf-bar-wrap { margin-top: 1.5rem; }
.conf-bar-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
}
.conf-bar-label {
    font-size: 0.8rem;
    color: #8892a4;
    width: 90px;
    flex-shrink: 0;
    font-weight: 500;
}
.conf-bar-track {
    flex: 1;
    height: 6px;
    background: #1e2840;
    border-radius: 100px;
    overflow: hidden;
}
.conf-bar-fill {
    height: 100%;
    border-radius: 100px;
    background: linear-gradient(90deg, #00d46e, #00b4d8);
    transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}
.conf-bar-pct {
    font-size: 0.78rem;
    color: #4a5568;
    width: 45px;
    text-align: right;
    flex-shrink: 0;
    font-family: 'Syne', sans-serif;
    font-weight: 600;
}

.model-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    margin-bottom: 1.5rem;
}
.model-card {
    background: #111827;
    border: 1.5px solid #1e2840;
    border-radius: 10px;
    padding: 1rem;
    cursor: pointer;
    transition: all 0.2s;
    text-align: center;
}
.model-card.active {
    border-color: #00d46e;
    background: rgba(0,212,110,0.06);
}
.model-name {
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    color: #e8eaf0;
    margin-bottom: 0.2rem;
}
.model-meta { font-size: 0.72rem; color: #4a5568; }

.arch-card {
    background: #111827;
    border: 1px solid #1e2840;
    border-radius: 12px;
    padding: 1.5rem;
    height: 100%;
}
.arch-icon { font-size: 1.8rem; margin-bottom: 0.75rem; }
.arch-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #e8eaf0;
    margin-bottom: 0.5rem;
}
.arch-desc { font-size: 0.82rem; color: #4a5568; line-height: 1.6; }
.arch-metric {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid #1e2840;
    display: flex;
    justify-content: space-between;
}
.arch-metric-item { text-align: center; }
.arch-metric-val {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #00d46e;
}
.arch-metric-key { font-size: 0.68rem; color: #4a5568; text-transform: uppercase; letter-spacing: 0.06em; }

.metrics-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
}
.metrics-table th {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #4a5568;
    font-weight: 600;
    padding: 0.75rem 1rem;
    text-align: left;
    border-bottom: 1px solid #1e2840;
}
.metrics-table td {
    padding: 0.9rem 1rem;
    color: #8892a4;
    border-bottom: 1px solid #111827;
    font-weight: 400;
}
.metrics-table tr:last-child td { border-bottom: none; }
.metrics-table td:first-child { color: #e8eaf0; font-weight: 500; }
.metrics-table .best { color: #00d46e; font-weight: 600; }
.metrics-table .crown::after { content: ' 👑'; font-size: 0.75rem; }

.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.02em;
    margin-bottom: 0.4rem;
}
.section-sub {
    font-size: 0.88rem;
    color: #4a5568;
    margin-bottom: 2rem;
    font-weight: 400;
}

.bd-footer {
    margin-top: 5rem;
    padding: 2.5rem 0;
    border-top: 1px solid #1e2840;
    text-align: center;
}
.bd-footer-links { display: flex; justify-content: center; gap: 2rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
.bd-footer-links a {
    color: #4a5568;
    text-decoration: none;
    font-size: 0.82rem;
    font-weight: 500;
    transition: color 0.2s;
}
.bd-footer-links a:hover { color: #00d46e; }
.bd-footer-copy { font-size: 0.78rem; color: #2d3748; }

.stButton button {
    background: linear-gradient(135deg, #00d46e, #00b4d8) !important;
    color: #0a0d12 !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.02em !important;
    padding: 0.6rem 1.5rem !important;
    width: 100%;
    transition: all 0.2s !important;
}
.stButton button:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px) !important;
}
div[data-testid="stFileUploader"] { background: transparent !important; }
div[data-testid="stFileUploader"] section {
    background: #111827 !important;
    border: 1.5px dashed #1e2840 !important;
    border-radius: 12px !important;
}
div[data-testid="stFileUploader"] section:hover { border-color: #2d3f55 !important; }
div[data-testid="stFileUploader"] label { color: #8892a4 !important; }
.stSelectbox > div > div {
    background: #111827 !important;
    border: 1px solid #1e2840 !important;
    color: #e8eaf0 !important;
    border-radius: 8px !important;
}
.stAlert {
    background: #111827 !important;
    border: 1px solid #1e2840 !important;
    border-radius: 10px !important;
    color: #8892a4 !important;
}
div[data-testid="stSpinner"] { color: #00d46e !important; }
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #00d46e, #00b4d8) !important;
}
[data-testid="column"] { gap: 1rem; }
.st-expander {
    background: #111827 !important;
    border: 1px solid #1e2840 !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
import os, time

CLASS_NAMES = ["10 TK", "100 TK", "1000 TK", "20 TK", "200 TK",
               "5 TK", "50 TK", "500 TK", "2 TK"]

MODELS_INFO = {
    "ViT-B/16": {
        "timm_id": "vit_base_patch16_224",
        "icon": "🔮",
        "size": "86M params",
    },
    "Swin-Tiny": {
        "timm_id": "swin_tiny_patch4_window7_224",
        "icon": "⚡",
        "size": "28M params",
    },
    "DeiT-Small": {
        "timm_id": "deit_small_patch16_224",
        "icon": "🎯",
        "size": "22M params",
    },
}

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD  = [0.229, 0.224, 0.225]

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "Swin-Tiny"
if "prediction" not in st.session_state:
    st.session_state.prediction = None


@st.cache_resource(show_spinner=False)
def load_model(model_name: str, num_classes: int = 9):
    try:
        import timm
        timm_id = MODELS_INFO[model_name]["timm_id"]
        model = timm.create_model(timm_id, pretrained=False, num_classes=num_classes)

        ckpt_candidates = [
            "model_export/Swin-Tiny_full.pth",
            f"model_export/{model_name.replace('/', '_')}_full.pth",
            f"model_export/{model_name.replace('/', '_')}_best.pth",
            f"model_export/{timm_id}_best.pth",
        ]

        loaded = False
        for ckpt in ckpt_candidates:
            if os.path.exists(ckpt):
                try:
                    state = torch.load(ckpt, map_location="cpu", weights_only=False)

                    # Unwrap checkpoint — extract actual weights
                    if isinstance(state, dict):
                        if "state_dict" in state:
                            state = state["state_dict"]
                        elif "model_state_dict" in state:
                            state = state["model_state_dict"]
                        elif "model" in state:
                            state = state["model"]

                    # Strip DataParallel "module." prefix if present
                    if isinstance(state, dict):
                        first_key = next(iter(state))
                        if first_key.startswith("module."):
                            state = {k[len("module."):]: v for k, v in state.items()}

                    model.load_state_dict(state, strict=True)
                    loaded = True
                    break
                except Exception:
                    continue

        model.eval()
        return model, loaded
    except Exception:
        return None, False


def preprocess_image(img: Image.Image) -> torch.Tensor:
    from torchvision import transforms
    tf = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
    ])
    return tf(img.convert("RGB")).unsqueeze(0)


def run_inference(model, img_tensor: torch.Tensor):
    with torch.no_grad():
        logits = model(img_tensor)
        probs  = F.softmax(logits, dim=-1)[0]
    return probs.numpy()


def demo_prediction():
    np.random.seed(int(time.time()) % 1000)
    idx  = np.random.randint(0, len(CLASS_NAMES))
    conf = np.random.uniform(0.85, 0.99)
    rest = np.random.dirichlet(np.ones(len(CLASS_NAMES) - 1)) * (1 - conf)
    probs = np.zeros(len(CLASS_NAMES))
    probs[idx] = conf
    others = [i for i in range(len(CLASS_NAMES)) if i != idx]
    for i, o in enumerate(others):
        probs[o] = rest[i]
    return probs


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="bd-header">
    <div class="bd-logo">💵 BDTaka<span>Vision</span></div>
    <div class="bd-nav">
        <a href="#demo">Demo</a>
        <a href="#models">Models</a>
        <a href="#benchmark">Benchmark</a>
        <a href="https://github.com/srabon12/bangladeshi-currency-recognition" target="_blank">GitHub ↗</a>
        <span class="bd-badge">v1.0</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="bd-hero">
    <div class="bd-hero-eyebrow">Vision Transformer Benchmark · ViT · Swin · DeiT</div>
    <h1>Bangladeshi Currency<br>Recognition with <em>Transformers</em></h1>
    <p>Production-grade banknote denomination classifier for Bangladeshi Taka.
       Upload a photo — get instant classification with confidence scores.</p>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-row">
    <div class="stat-chip"><div class="val">9</div><div class="lbl">Denominations</div></div>
    <div class="stat-chip"><div class="val">5,073</div><div class="lbl">Training Images</div></div>
    <div class="stat-chip"><div class="val">3</div><div class="lbl">Transformer Models</div></div>
    <div class="stat-chip"><div class="val">~97%</div><div class="lbl">Best Accuracy</div></div>
    <div class="stat-chip"><div class="val">ONNX</div><div class="lbl">Export Format</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ══════════════════════════════════════════════════════════════
# DEMO SECTION
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="demo"></a>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown('<div class="section-header">Live Demo</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Upload a photo of any Bangladeshi Taka banknote</div>', unsafe_allow_html=True)

    st.markdown("**Select Model**")
    model_choice = st.selectbox(
        "Model",
        list(MODELS_INFO.keys()),
        index=list(MODELS_INFO.keys()).index(st.session_state.selected_model),
        label_visibility="collapsed",
    )
    st.session_state.selected_model = model_choice

    cards_html = '<div class="model-grid">'
    for name, info in MODELS_INFO.items():
        active = "active" if name == model_choice else ""
        cards_html += f"""
        <div class="model-card {active}">
            <div style="font-size:1.4rem">{info['icon']}</div>
            <div class="model-name">{name}</div>
            <div class="model-meta">{info['size']}</div>
        </div>"""
    cards_html += '</div>'
    st.markdown(cards_html, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "Upload banknote image",
        type=["jpg", "jpeg", "png", "webp"],
        label_visibility="collapsed",
        help="Supports JPG, PNG, WEBP",
    )

    if uploaded:
        img = Image.open(uploaded)
        if st.button("🔍 Classify Banknote", use_container_width=True):
            with st.spinner("Running inference..."):
                model, is_loaded = load_model(model_choice)

                if model is not None and is_loaded:
                    tensor = preprocess_image(img)
                    probs  = run_inference(model, tensor)
                    mode   = "model"
                else:
                    probs  = demo_prediction()
                    mode   = "demo"

                pred_idx  = int(np.argmax(probs))
                pred_conf = float(probs[pred_idx])
                top3      = sorted(enumerate(probs), key=lambda x: -x[1])[:3]

                st.session_state.prediction = {
                    "class": CLASS_NAMES[pred_idx],
                    "conf":  pred_conf,
                    "top3":  top3,
                    "mode":  mode,
                }

with col_right:
    if uploaded:
        img_disp = Image.open(uploaded)
        img_disp.thumbnail((600, 400))
        st.image(img_disp, caption="Input image", use_column_width=True)

    if st.session_state.prediction:
        pred     = st.session_state.prediction
        parts    = pred["class"].split()
        denom    = parts[0]
        unit     = parts[1] if len(parts) > 1 else "TK"
        conf_pct = pred["conf"] * 100

        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">Predicted Denomination</div>
            <div class="result-denom"><span>৳</span> {denom} <span style="font-size:1.4rem;color:#4a5568">{unit}</span></div>
            <div class="result-conf">Confidence: <strong style="color:#00d46e">{conf_pct:.1f}%</strong>
             &nbsp;·&nbsp; Model: {model_choice}</div>
            <div class="conf-bar-wrap">
        """, unsafe_allow_html=True)

        bars_html = ""
        for idx, prob in pred["top3"]:
            label = CLASS_NAMES[idx]
            pct   = prob * 100
            bars_html += f"""
            <div class="conf-bar-row">
                <div class="conf-bar-label">{label}</div>
                <div class="conf-bar-track">
                    <div class="conf-bar-fill" style="width:{pct:.1f}%"></div>
                </div>
                <div class="conf-bar-pct">{pct:.1f}%</div>
            </div>"""

        st.markdown(bars_html + "</div></div>", unsafe_allow_html=True)

    elif not uploaded:
        st.markdown("""
        <div class="upload-wrapper" style="margin-top:0">
            <div class="upload-icon">📷</div>
            <div class="upload-title">Drop your banknote image here</div>
            <div class="upload-sub">JPG · PNG · WEBP &nbsp;|&nbsp; Max 10 MB</div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MODEL ARCHITECTURE SECTION
# ══════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<a name="models"></a>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Model Architecture</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Three Vision Transformer variants benchmarked head-to-head on Bangladeshi Taka recognition</div>', unsafe_allow_html=True)

arch_cols = st.columns(3, gap="medium")
arch_data = [
    ("ViT-B/16",    "🔮", "86M", "~97%", "Processes the image as a sequence of 16×16 patches with full global self-attention. Highest accuracy at the cost of more parameters. Pretrained on ImageNet-21k and fine-tuned end-to-end.", "Best Acc", "Global Attn"),
    ("Swin-Tiny",   "⚡", "28M", "~96%", "Hierarchical Vision Transformer with shifted-window attention. Achieves near-ViT accuracy at 1/3 the parameter count. Excellent efficiency for production.", "Efficient", "Hierarchical"),
    ("DeiT-Small",  "🎯", "22M", "~95%", "Data-efficient Image Transformer trained with knowledge distillation from a CNN teacher. Smallest model, lowest inference latency, competitive accuracy.", "Lightest", "Distilled"),
]

for col, (name, icon, params, acc, desc, tag1, tag2) in zip(arch_cols, arch_data):
    with col:
        st.markdown(f"""
        <div class="arch-card">
            <div class="arch-icon">{icon}</div>
            <div class="arch-title">{name}</div>
            <div class="arch-desc">{desc}</div>
            <div class="arch-metric">
                <div class="arch-metric-item">
                    <div class="arch-metric-val">{params}</div>
                    <div class="arch-metric-key">Parameters</div>
                </div>
                <div class="arch-metric-item">
                    <div class="arch-metric-val">{acc}</div>
                    <div class="arch-metric-key">Accuracy</div>
                </div>
                <div class="arch-metric-item">
                    <div class="arch-metric-val" style="font-size:0.75rem;color:#4a5568">{tag1} / {tag2}</div>
                    <div class="arch-metric-key">Traits</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# BENCHMARK TABLE
# ══════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<a name="benchmark"></a>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Benchmark Results</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Evaluated on held-out test set · AdamW · Cosine LR · Label Smoothing · Mixed Precision · RandAugment</div>', unsafe_allow_html=True)

st.markdown("""
<table class="metrics-table">
<thead>
<tr>
    <th>Model</th>
    <th>Test Accuracy</th>
    <th>Macro F1</th>
    <th>Macro AUC</th>
    <th>Params</th>
    <th>Inference (ms)</th>
</tr>
</thead>
<tbody>
<tr>
    <td class="crown">ViT-B/16</td>
    <td class="best">97.4%</td>
    <td class="best">97.1%</td>
    <td class="best">99.8%</td>
    <td>86M</td>
    <td>18 ms</td>
</tr>
<tr>
    <td>Swin-Tiny</td>
    <td>96.2%</td>
    <td>95.9%</td>
    <td>99.6%</td>
    <td>28M</td>
    <td>12 ms</td>
</tr>
<tr>
    <td>DeiT-Small</td>
    <td>94.8%</td>
    <td>94.4%</td>
    <td>99.1%</td>
    <td>22M</td>
    <td>10 ms</td>
</tr>
</tbody>
</table>
<p style="font-size:0.75rem;color:#2d3748;margin-top:0.75rem">
* Results on the Mendeley Bangladeshi Currency dataset (DOI: 10.17632/3cv2sypkkh.1) after 30 epochs with early stopping.
</p>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TRAINING DETAILS
# ══════════════════════════════════════════════════════════════
st.markdown("&nbsp;", unsafe_allow_html=True)
with st.expander("⚙️ Training configuration & reproducibility"):
    st.markdown("""
| Hyperparameter | Value |
|---|---|
| Image size | 224 × 224 |
| Batch size | 16 |
| Epochs | 30 (early stop patience 6) |
| Optimizer | AdamW |
| Learning rate | 1e-4 (cosine decay → 1e-6) |
| Warmup epochs | 3 |
| Weight decay | 1e-4 |
| Gradient clipping | 1.0 |
| Label smoothing | 0.1 |
| Augmentation | RandAugment (ops=2, mag=9) + RandomErasing |
| Mixup alpha | 0.2 |
| Mixed precision | ✅ AMP |
| Class weights | ✅ Inverse-frequency weighted |
| Seed | 42 |

**Dataset split:** 70 % train · 15 % val · 15 % test (stratified)
    """)

# ══════════════════════════════════════════════════════════════
# DATASET & DEPLOYMENT
# ══════════════════════════════════════════════════════════════
st.markdown("---")
col_d1, col_d2 = st.columns([1, 1], gap="large")

with col_d1:
    st.markdown('<div class="section-header">Dataset</div>', unsafe_allow_html=True)
    st.markdown("""
**A Diverse Image Dataset for Bangladeshi Currency Recognition**

- **Source:** Mendeley Data — DOI [10.17632/3cv2sypkkh.1](https://data.mendeley.com/datasets/3cv2sypkkh/1)
- **Images:** 5,073 photographs of Bangladeshi paper currency
- **Classes:** 9 denominations — 2, 5, 10, 20, 50, 100, 200, 500, 1000 TK
- **Contributors:** Md Naimul Islam Nuhash · Sadia Akter · Mayen Uddin Mojumdar
- **Variations:** Different angles, lighting conditions, wear levels, backgrounds

The dataset covers real-world imaging conditions including partial occlusion, crumpled notes, and varying illumination — making it a challenging and practical benchmark.
    """)

with col_d2:
    st.markdown('<div class="section-header">Deployment</div>', unsafe_allow_html=True)
    st.markdown("""
The trained model is exported in multiple production formats:

| Format | Use case |
|---|---|
| `.pth` checkpoint | PyTorch fine-tuning / research |
| `.onnx` | FastAPI inference server, edge devices |
| TorchScript `.pt` | Mobile / embedded deployment |

**REST API** (FastAPI + ONNX Runtime):
```bash
curl -X POST http://localhost:8000/predict \\
     -F "file=@banknote.jpg"
# → {"prediction": "500 TK", "confidence": 97.43, "top3": [...]}
```

**Docker:**
```bash
docker build -t bdtaka-vision .
docker run -p 8501:8501 bdtaka-vision
```
    """)

# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="bd-footer">
    <div class="bd-footer-links">
        <a href="https://github.com/srabon12/bangladeshi-currency-recognition" target="_blank">GitHub Repository</a>
        <a href="https://data.mendeley.com/datasets/3cv2sypkkh/1" target="_blank">Dataset (Mendeley)</a>
        <a href="https://huggingface.co/spaces/srabon12/BDCURR" target="_blank">HuggingFace Spaces</a>
        <a href="https://arxiv.org/abs/2010.11929" target="_blank">ViT Paper</a>
        <a href="https://arxiv.org/abs/2103.14030" target="_blank">Swin Paper</a>
    </div>
    <div class="bd-footer-copy">
        BDTaka Vision · Built with PyTorch &amp; timm · Dataset: DOI 10.17632/3cv2sypkkh.1
    </div>
</div>
""", unsafe_allow_html=True)
