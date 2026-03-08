import streamlit as st
from utils import generate_challange, generate_seed

st.set_page_config(page_title="FotoDice", page_icon="📸", layout="centered")

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Space+Mono:wght@400;700&display=swap');

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }

/* Page background */
.stApp {
    background: #0D0B09;
    color: #F0E4C8;
}

/* Kill default padding */
.block-container {
    padding-top: 0 !important;
    max-width: 520px !important;
}

/* ── HEADER ── */
.foto-header {
    text-align: center;
    padding: 56px 0 8px;
}
.foto-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.4em;
    color: #B8956A;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.foto-title {
    font-family: 'Playfair Display', serif;
    font-size: 72px;
    font-weight: 700;
    color: #E8D5B0;
    margin: 0;
    line-height: 1;
}
.foto-title span { color: #C9A96E; }
.foto-subtitle {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 16px;
    color: #B8956A;
    margin-top: 14px;
}

/* ── ROLL BUTTON ── */
div[data-testid="stButton"] > button {
    width: 100%;
    background: transparent !important;
    border: 1.5px solid #C9A96E !important;
    color: #C9A96E !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
    letter-spacing: 0.25em !important;
    text-transform: uppercase !important;
    padding: 18px 0 !important;
    border-radius: 0 !important;
    transition: all 0.2s !important;
}
div[data-testid="stButton"] > button:hover {
    background: #C9A96E !important;
    color: #0D0B09 !important;
}

/* ── EXPANDER (Have an ID?) ── */
[data-testid="stExpander"] {
    border: none !important;
    background: transparent !important;
}
[data-testid="stExpander"] summary {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.2em;
    color: #A07850 !important;
    text-transform: uppercase;
    padding: 8px 0 !important;
}
[data-testid="stExpander"] summary:hover {
    color: #C9A96E !important;
}
[data-testid="stExpander"] > div > div {
    border-top: 1px solid rgba(232,213,176,0.08) !important;
    padding-top: 16px !important;
}

/* ── NUMBER INPUT ── */
[data-testid="stNumberInput"] input {
    background: #1A1612 !important;
    border: 1px solid rgba(232,213,176,0.25) !important;
    border-radius: 0 !important;
    color: #F0E4C8 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 15px !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: #C9A96E !important;
    box-shadow: none !important;
}
[data-testid="stNumberInput"] label {
    color: #A89070 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 11px !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
}
[data-testid="stNumberInput"] button {
    background: #1A1612 !important;
    border-color: rgba(232,213,176,0.2) !important;
    color: #A89070 !important;
}

/* ── CHALLENGE CARD ── */
.challenge-card {
    border: 1px solid rgba(201,169,110,0.3);
    background: rgba(201,169,110,0.04);
    padding: 32px 28px;
    margin: 28px 0;
    position: relative;
}
.challenge-card::before,
.challenge-card::after {
    content: '';
    position: absolute;
    width: 16px;
    height: 16px;
}
.challenge-card::before {
    top: -1px; left: -1px;
    border-top: 2px solid #C9A96E;
    border-left: 2px solid #C9A96E;
}
.challenge-card::after {
    bottom: -1px; right: -1px;
    border-bottom: 2px solid #C9A96E;
    border-right: 2px solid #C9A96E;
}
.card-id {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.4em;
    color: #B8956A;
    text-transform: uppercase;
    margin-bottom: 24px;
}
.card-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 12px 0;
    border-bottom: 1px solid rgba(232,213,176,0.07);
}
.card-row:last-of-type { border-bottom: none; }
.card-label {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    min-width: 110px;
}
.card-value {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 17px;
    color: #E8D5B0;
    text-align: right;
}

/* ── HASHTAG BOX ── */
.hashtag-box {
    border: 1px solid rgba(232,213,176,0.15);
    background: rgba(232,213,176,0.03);
    padding: 14px 18px;
    margin-top: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.hashtag-text {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: #C9A96E;
}
.share-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.3em;
    color: #B8956A;
    text-transform: uppercase;
    margin-bottom: 10px;
    margin-top: 24px;
}

/* ── HOW IT WORKS ── */
.how-section {
    margin-top: 48px;
    border-top: 1px solid rgba(232,213,176,0.08);
    padding-top: 32px;
}
.how-title {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.35em;
    color: #B8956A;
    text-transform: uppercase;
    margin-bottom: 24px;
}
.how-step {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
}
.how-num {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #A07850;
    padding-top: 2px;
    min-width: 24px;
}
.how-step-title {
    font-family: 'Playfair Display', serif;
    font-size: 15px;
    color: #C9A96E;
    margin-bottom: 4px;
}
.how-step-desc {
    font-family: 'Playfair Display', serif;
    font-size: 13px;
    color: #A07850;
    line-height: 1.6;
    font-style: italic;
}

/* ── FILMSTRIP ── */
.filmstrip {
    display: flex;
    gap: 0;
    padding: 10px 0;
    overflow: hidden;
    border-bottom: 2px solid #C9A96E;
    border-top: 2px solid #C9A96E;
    margin-bottom: 0;
    background: #1a1410;
}
.filmstrip-hole {
    width: 14px;
    height: 22px;
    border-radius: 3px;
    background: #0D0B09;
    border: 1.5px solid #C9A96E;
    display: inline-block;
    margin: 0 5px;
    flex-shrink: 0;
    opacity: 0.7;
}
</style>
""", unsafe_allow_html=True)

# ── FILMSTRIP TOP ──────────────────────────────────────────────────────────
holes = '<div class="filmstrip">' + '<span class="filmstrip-hole"></span>' * 40 + '</div>'
st.markdown(f'<div style="background:#111;margin:-1rem -1rem 0">{holes}</div>', unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="foto-header">
    <div class="foto-eyebrow">— a photographer's dice —</div>
    <h1 class="foto-title">Foto<span>Dice</span></h1>
    <p class="foto-subtitle">Roll the rules.&ensp;Shoot the photo.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────
if "result" not in st.session_state:
    st.session_state.result = None
    st.session_state.seed = None

# ── ROLL BUTTON ───────────────────────────────────────────────────────────
if st.button("🎲  Roll the Dice", use_container_width=True):
    seed = generate_seed()
    st.session_state.result = generate_challange(seed)
    st.session_state.seed = seed

# ── HAVE AN ID? ───────────────────────────────────────────────────────────
with st.expander("↳  Have a Challenge ID?"):
    challenge_id = st.number_input(
        "Enter ID (10000 – 34487)",
        min_value=10000,
        max_value=34487,
        value=10000,
        step=1,
        label_visibility="visible"
    )
    if st.button("Load challenge", use_container_width=True):
        st.session_state.result = generate_challange(challenge_id)
        st.session_state.seed = challenge_id

# ── CHALLENGE CARD ────────────────────────────────────────────────────────
LABEL_COLORS = ["#E8D5B0", "#C9A96E", "#C9956A", "#C9A96E", "#E8D5B0"]

if st.session_state.result:
    result = st.session_state.result
    seed = st.session_state.seed

    fields = ["Format", "Orientation", "Color", "Subject", "Time of Day"]

    st.markdown(f'<div class="challenge-card"><div class="card-id">Challenge #{seed}</div>' + 
        "".join([
            f'<div class="card-row"><span class="card-label" style="color:{LABEL_COLORS[i]}">{key}</span><span class="card-value">{result[key]}</span></div>'
            for i, key in enumerate(fields)
        ]) + '</div>', unsafe_allow_html=True)

    # Share
    st.markdown('<div class="share-label">Share your shot</div>', unsafe_allow_html=True)
    tags = f"#FotoDice #FotoDice{seed}"
    st.markdown(f"""
    <div class="hashtag-box">
        <span class="hashtag-text">{tags}</span>
    </div>
    """, unsafe_allow_html=True)
    st.code(tags, language=None)

# ── HOW IT WORKS ──────────────────────────────────────────────────────────
if not st.session_state.result:
    st.markdown("""
    <div class="how-section">
        <div class="how-title">How it works</div>
        <div class="how-step">
            <span class="how-num">01</span>
            <div>
                <div class="how-step-title">Roll</div>
                <div class="how-step-desc">Generate your unique combination of format, orientation, color, theme and time of day.</div>
            </div>
        </div>
        <div class="how-step">
            <span class="how-num">02</span>
            <div>
                <div class="how-step-title">Shoot</div>
                <div class="how-step-desc">Take photos guided by these rules. Limitations breed creativity.</div>
            </div>
        </div>
        <div class="how-step">
            <span class="how-num">03</span>
            <div>
                <div class="how-step-title">Share</div>
                <div class="how-step-desc">Post with your Challenge ID so others can attempt the same roll.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)