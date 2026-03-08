import streamlit as st
from utils import generate_challange, generate_seed
from datetime import datetime

st.set_page_config(page_title="FotoDice", page_icon="📸", layout="centered")

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }

:root {
    --bg:        #1C1C1E;
    --bg-card:   #242426;
    --bg-lift:   #2C2C2E;
    --accent:    #FF9500;
    --accent-hi: #FFB340;
    --text:      #F5F5F0;
    --text-muted:#8E8E93;
    --text-dim:  #48484A;
    --border:    rgba(245,245,240,0.08);
    --radius:    12px;
}

.stApp {
    background: var(--bg);
    color: var(--text);
}
.block-container {
    padding-top: 0 !important;
    max-width: 480px !important;
}

/* Grain overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9999;
    opacity: 0.035;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
    background-size: 128px;
}

/* Header */
.foto-header {
    padding: 52px 0 4px;
    text-align: left;
}
.foto-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.22em;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 10px;
}
.foto-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 56px;
    font-weight: 600;
    color: var(--text);
    margin: 0;
    line-height: 1.05;
    letter-spacing: -0.03em;
}
.foto-title span { color: var(--accent); }
.foto-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    color: var(--text-muted);
    margin-top: 10px;
    font-weight: 300;
}

/* Roll button */
div[data-testid="stButton"] > button {
    width: 100%;
    background: var(--accent) !important;
    border: none !important;
    color: #1C1C1E !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    padding: 16px 0 !important;
    border-radius: var(--radius) !important;
    transition: background 0.15s, transform 0.1s !important;
}
div[data-testid="stButton"] > button:hover {
    background: var(--accent-hi) !important;
    transform: translateY(-1px) !important;
}
div[data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
}

/* Expander */
[data-testid="stExpander"] {
    border: 1px solid var(--border) !important;
    background: var(--bg-card) !important;
    border-radius: var(--radius) !important;
}
[data-testid="stExpander"] summary {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    color: var(--text-muted) !important;
    text-transform: uppercase;
    padding: 14px 16px !important;
}
[data-testid="stExpander"] summary:hover { color: var(--text) !important; }
[data-testid="stExpander"] > div > div {
    padding: 0 16px 16px !important;
    border-top: 1px solid var(--border) !important;
}

/* Number input */
[data-testid="stNumberInput"] input {
    background: var(--bg-lift) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 14px !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(255,149,0,0.12) !important;
}
[data-testid="stNumberInput"] label {
    color: var(--text-muted) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
}
[data-testid="stNumberInput"] button {
    background: var(--bg-lift) !important;
    border-color: var(--border) !important;
    color: var(--text-muted) !important;
}

/* Challenge card */
.challenge-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    margin: 24px 0 0;
}
.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    background: var(--bg-lift);
}
.card-id {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.2em;
    color: var(--accent);
    text-transform: uppercase;
}
.card-timestamp {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--text-dim);
}
.card-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 13px 20px;
    border-bottom: 1px solid var(--border);
}
.card-row:last-of-type { border-bottom: none; }
.card-label {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--text-muted);
}
.card-value {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    font-weight: 500;
    color: var(--text);
}

/* Share */
.share-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    color: var(--text-muted);
    text-transform: uppercase;
    margin: 20px 0 8px;
}
.hashtag-box {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
}
.hashtag-text {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: var(--accent);
}

/* How it works — compact strip */
.how-strip {
    display: flex;
    gap: 0;
    margin: 20px 0 24px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
}
.how-strip-step {
    flex: 1;
    padding: 16px 14px;
    border-right: 1px solid var(--border);
    position: relative;
}
.how-strip-step:last-child { border-right: none; }
.how-strip-icon {
    font-size: 20px;
    margin-bottom: 8px;
    display: block;
}
.how-strip-num {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    color: var(--accent);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 4px;
    display: block;
}
.how-strip-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 4px;
}
.how-strip-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    color: var(--text-muted);
    line-height: 1.45;
    font-weight: 300;
}

/* Filmstrip */
.filmstrip {
    display: flex;
    padding: 8px 0;
    overflow: hidden;
    border-bottom: 2px solid rgba(255,149,0,0.2);
    border-top: 2px solid rgba(255,149,0,0.2);
    background: #161618;
}
.filmstrip-hole {
    width: 12px;
    height: 18px;
    border-radius: 3px;
    background: var(--bg);
    border: 1px solid rgba(255,149,0,0.15);
    display: inline-block;
    margin: 0 5px;
    flex-shrink: 0;
}
</style>
""", unsafe_allow_html=True)

# ── FILMSTRIP ─────────────────────────────────────────────────────────────
holes = '<div class="filmstrip">' + '<span class="filmstrip-hole"></span>' * 40 + '</div>'
st.markdown(f'<div style="background:#111;margin:-1rem -1rem 0">{holes}</div>', unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="foto-header">
    <div class="foto-eyebrow">⚡ a photographer's dice</div>
    <h1 class="foto-title">Foto<span>Dice</span></h1>
    <p class="foto-subtitle">Roll your shot parameters — format, color, subject, time of day — then go shoot.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────
if "result" not in st.session_state:
    st.session_state.result = None
    st.session_state.seed = None

# ── HOW IT WORKS STRIP (always visible) ───────────────────────────────────
st.markdown("""
<div class="how-strip">
    <div class="how-strip-step">
        <span class="how-strip-icon">🎲</span>
        <span class="how-strip-num">01 · Roll</span>
        <div class="how-strip-title">Get your challenge</div>
        <div class="how-strip-desc">Format, color, subject & time of day — all randomized in one click.</div>
    </div>
    <div class="how-strip-step">
        <span class="how-strip-icon">📷</span>
        <span class="how-strip-num">02 · Shoot</span>
        <div class="how-strip-title">Go out & shoot</div>
        <div class="how-strip-desc">Let the rules guide you. Constraints breed creativity.</div>
    </div>
    <div class="how-strip-step">
        <span class="how-strip-icon">🏷️</span>
        <span class="how-strip-num">03 · Share</span>
        <div class="how-strip-title">Post your shot</div>
        <div class="how-strip-desc">Tag your ID so others can try the same roll.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ROLL BUTTON ───────────────────────────────────────────────────────────
if st.button("⚡  Roll the Dice", use_container_width=True):
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
if st.session_state.result:
    result = st.session_state.result
    seed = st.session_state.seed
    now = datetime.now().strftime("%Y-%m-%d  %H:%M")

    fields = ["Format", "Orientation", "Color", "Subject", "Time of Day"]

    rows_html = "".join([
        f'<div class="card-row"><span class="card-label">{key}</span><span class="card-value">{result[key]}</span></div>'
        for key in fields
    ])

    st.markdown(f"""
    <div class="challenge-card">
        <div class="card-header">
            <span class="card-id">#{seed}</span>
            <span class="card-timestamp">{now}</span>
        </div>
        <div class="card-body">
            {rows_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

    tags = f"#FotoDice #FotoDice{seed}"
    st.markdown('<div class="share-label">Share your shot</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="hashtag-box">
        <span class="hashtag-text">{tags}</span>
    </div>
    """, unsafe_allow_html=True)
    st.code(tags, language=None)