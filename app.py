import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime

# ─────────────────────────────────────────
# INIT
# ─────────────────────────────────────────
load_dotenv()

st.set_page_config(
    page_title="ICANG AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
# CUSTOM CSS — style sesuai index.php
# ─────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">

<style>
/* ── VARIABLES ── */
:root {
  --bg:     #0D0D0D;
  --bg2:    #141414;
  --bg3:    #1a1a1a;
  --bg4:    #222;
  --fg:     #F5F5F0;
  --fg2:    #aaa;
  --fg3:    #555;
  --yellow: #F5E642;
  --red:    #FF3366;
  --green:  #00F5A0;
  --border: #2a2a2a;
  --radius: 8px;
  --radius-lg: 12px;
}

/* ── GLOBAL ── */
html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"] {
  background: var(--bg) !important;
  color: var(--fg) !important;
  font-family: 'Space Grotesk', sans-serif !important;
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, footer, header,
[data-testid="stDeployButton"],
[data-testid="stDecoration"] { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: var(--bg2) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--fg) !important; }

/* Sidebar nav buttons */
[data-testid="stSidebar"] .stButton > button {
  width: 100%;
  background: transparent !important;
  border: 1px solid var(--border) !important;
  color: var(--fg2) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  padding: 10px 14px !important;
  border-radius: var(--radius) !important;
  text-align: left !important;
  transition: all .2s !important;
  margin-bottom: 4px !important;
  letter-spacing: .04em !important;
  text-transform: uppercase !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
  border-color: var(--yellow) !important;
  color: var(--yellow) !important;
  background: rgba(245,230,66,.06) !important;
}

/* Sidebar active page button */
[data-testid="stSidebar"] .stButton > button[kind="primary"] {
  border-color: var(--yellow) !important;
  background: rgba(245,230,66,.12) !important;
  color: var(--yellow) !important;
}

/* Clear history button */
.clear-btn > button {
  background: transparent !important;
  border: 1px solid var(--red) !important;
  color: var(--red) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-size: 12px !important;
  font-weight: 600 !important;
  border-radius: var(--radius) !important;
  width: 100% !important;
  padding: 8px !important;
  letter-spacing: .04em !important;
  text-transform: uppercase !important;
}
.clear-btn > button:hover {
  background: var(--red) !important;
  color: #fff !important;
}

/* ── MAIN CONTENT AREA ── */
[data-testid="stMainBlockContainer"] {
  background: var(--bg) !important;
  padding: 0 !important;
  max-width: 100% !important;
}
.block-container {
  padding: 0 !important;
  max-width: 100% !important;
}

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] {
  background: transparent !important;
  border: none !important;
  padding: 6px 0 !important;
}

/* User bubble */
[data-testid="stChatMessage"][data-testid*="user"],
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
  flex-direction: row-reverse !important;
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stMarkdown {
  background: rgba(245,230,66,.1) !important;
  border: 1px solid rgba(245,230,66,.25) !important;
  border-radius: var(--radius-lg) var(--radius-lg) 0 var(--radius-lg) !important;
  padding: 12px 16px !important;
  color: var(--fg) !important;
  font-size: 14px !important;
  line-height: 1.65 !important;
}

/* AI bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) .stMarkdown {
  background: var(--bg2) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-lg) var(--radius-lg) var(--radius-lg) 0 !important;
  padding: 12px 16px !important;
  color: var(--fg) !important;
  font-size: 14px !important;
  line-height: 1.65 !important;
}

/* Avatar icons */
[data-testid="chatAvatarIcon-user"] {
  background: rgba(245,230,66,.15) !important;
  border: 1px solid rgba(245,230,66,.3) !important;
  color: var(--yellow) !important;
  border-radius: 50% !important;
}
[data-testid="chatAvatarIcon-assistant"] {
  background: rgba(255,51,102,.12) !important;
  border: 1px solid rgba(255,51,102,.3) !important;
  color: var(--red) !important;
  border-radius: 50% !important;
}

/* ── CHAT INPUT ── */
[data-testid="stChatInputContainer"] {
  background: var(--bg2) !important;
  border-top: 1px solid var(--border) !important;
  padding: 12px 20px !important;
}
[data-testid="stChatInputContainer"] textarea {
  background: var(--bg3) !important;
  border: 1px solid var(--border) !important;
  color: var(--fg) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-size: 14px !important;
  border-radius: var(--radius) !important;
}
[data-testid="stChatInputContainer"] textarea:focus {
  border-color: var(--yellow) !important;
  box-shadow: none !important;
}
[data-testid="stChatInputContainer"] button {
  background: var(--yellow) !important;
  color: #000 !important;
  border: none !important;
  border-radius: var(--radius) !important;
}
[data-testid="stChatInputContainer"] button:hover {
  background: #e0d020 !important;
}

/* ── TEXT INPUT (non-chat) ── */
.stTextInput input, .stTextArea textarea, .stSelectbox select {
  background: var(--bg3) !important;
  border: 1px solid var(--border) !important;
  color: var(--fg) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  border-radius: var(--radius) !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--yellow) !important;
  box-shadow: none !important;
}

/* ── SUBMIT BUTTON (non-chat) ── */
.stForm .stButton > button,
.main-btn > button {
  background: var(--yellow) !important;
  color: #000 !important;
  border: 1.5px solid var(--yellow) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 700 !important;
  font-size: 14px !important;
  letter-spacing: .06em !important;
  text-transform: uppercase !important;
  border-radius: var(--radius) !important;
  padding: 10px 20px !important;
  transition: all .2s !important;
}
.stForm .stButton > button:hover,
.main-btn > button:hover {
  background: transparent !important;
  color: var(--yellow) !important;
}

/* ── SPINNERS, ALERTS ── */
[data-testid="stSpinner"] { color: var(--yellow) !important; }
.stAlert { border-radius: var(--radius) !important; }

/* ── DIVIDER ── */
hr { border-color: var(--border) !important; }

/* ── LABELS ── */
.stTextInput label, .stTextArea label,
.stSelectbox label, .stNumberInput label {
  color: var(--fg2) !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  letter-spacing: .05em !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--fg3); }

/* ── CODE BLOCKS ── */
code, pre {
  background: var(--bg3) !important;
  color: var(--green) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  font-size: 13px !important;
}

/* ── PAGE HEADER ── */
.page-header {
  background: var(--bg2);
  border-bottom: 1px solid var(--border);
  padding: 20px 28px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.page-header-icon {
  font-size: 1.6rem;
  color: var(--yellow);
}
.page-header-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.6rem;
  color: var(--fg);
  letter-spacing: .05em;
  line-height: 1;
}
.page-header-sub {
  font-size: 12px;
  color: var(--fg3);
  margin-top: 2px;
}

/* ── CHAT WRAPPER ── */
.chat-wrap {
  padding: 20px 28px;
}

/* ── EMPTY STATE ── */
.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: var(--fg3);
}
.empty-state .icon {
  font-size: 3rem;
  margin-bottom: 12px;
  color: var(--border);
}
.empty-state h3 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.4rem;
  letter-spacing: .05em;
  color: var(--fg3);
  margin-bottom: 6px;
}
.empty-state p {
  font-size: 13px;
  color: var(--fg3);
}

/* ── MATH PAGE ── */
.result-card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  margin-top: 12px;
}
.result-card .label {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--fg3);
  margin-bottom: 8px;
}
.result-card .value {
  font-size: 15px;
  color: var(--fg);
  line-height: 1.7;
}

/* ── STORY PAGE ── */
.story-output {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-left: 3px solid var(--yellow);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  margin-top: 12px;
  font-size: 14px;
  line-height: 1.8;
  color: var(--fg2);
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# GOOGLE AI INIT
# ─────────────────────────────────────────
@st.cache_resource
def init_model():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("⚠ GOOGLE_API_KEY tidak ditemukan di file .env")
        st.stop()
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.5-flash")

model = init_model()


# ─────────────────────────────────────────
# SESSION STATE DEFAULTS
# ─────────────────────────────────────────
def init_state():
    defaults = {
        "halaman": "info",
        "chat_history": [],       # [{role, content, time}]
        "cerita_history": [],
        "math_history": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ─────────────────────────────────────────
# HELPER: CALL AI
# ─────────────────────────────────────────
def ask_ai(prompt: str, system: str = "") -> str:
    full_prompt = f"{system}\n\n{prompt}" if system else prompt
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"


def now_str() -> str:
    return datetime.now().strftime("%H:%M")


# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    # Logo
    st.markdown("""
    <div style="padding:8px 0 20px">
        <div style="font-family:'Bebas Neue',sans-serif;font-size:1.8rem;
                    color:#F5E642;text-shadow:2px 2px 0 #FF3366;
                    letter-spacing:.05em;line-height:1">
            ⚡ ICANG AI
        </div>
        <div style="font-size:12px;color:#555;margin-top:4px">
            Powered by Gemini 2.5 Flash
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Nav
    pages = [
        ("info",       "📰  Cari Berita"),
        ("cerita",     "📝  Buat Cerita"),
        ("matematika", "🧮  Hitung Matematika"),
    ]
    for key, label in pages:
        active = st.session_state["halaman"] == key
        btn_type = "primary" if active else "secondary"
        if st.button(label, key=f"nav_{key}", type=btn_type, use_container_width=True):
            st.session_state["halaman"] = key
            st.rerun()

    st.divider()

    # History stats
    halaman = st.session_state["halaman"]
    hist_key = {
        "info": "chat_history",
        "cerita": "cerita_history",
        "matematika": "math_history",
    }[halaman]

    n_msg = len(st.session_state[hist_key])

    st.markdown(f"""
    <div style="font-size:11px;letter-spacing:.1em;text-transform:uppercase;
                color:#555;margin-bottom:10px;font-weight:700">
        Riwayat
    </div>
    <div style="font-size:13px;color:#aaa;margin-bottom:12px">
        {n_msg // 2 if halaman == 'info' else n_msg} percakapan tersimpan
    </div>
    """, unsafe_allow_html=True)

    # Preview recent history items (info/chat only)
    if halaman == "info" and st.session_state["chat_history"]:
        user_msgs = [m for m in st.session_state["chat_history"] if m["role"] == "user"]
        for msg in user_msgs[-5:][::-1]:
            preview = msg["content"][:40] + "…" if len(msg["content"]) > 40 else msg["content"]
            st.markdown(f"""
            <div style="font-size:12px;color:#555;padding:6px 10px;
                        border:1px solid #2a2a2a;border-radius:6px;
                        margin-bottom:4px;white-space:nowrap;
                        overflow:hidden;text-overflow:ellipsis;">
                💬 {preview}
            </div>
            """, unsafe_allow_html=True)

    # Clear history button
    if n_msg > 0:
        st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
        if st.button("🗑 Hapus Riwayat", key="clear_hist", use_container_width=True):
            st.session_state[hist_key] = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown('<div style="font-size:11px;color:#333;text-align:center">ICANG AI © 2025</div>',
                unsafe_allow_html=True)


# ─────────────────────────────────────────
# PAGE: CARI BERITA (chat)
# ─────────────────────────────────────────
def page_info():
    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">📰</div>
        <div>
            <div class="page-header-title">Cari Berita & Info</div>
            <div class="page-header-sub">Tanya apa saja — berita, fakta, penjelasan</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    SYSTEM = (
        "Kamu adalah asisten AI bernama ICANG yang ramah dan informatif. "
        "Jawab dalam Bahasa Indonesia, singkat tapi lengkap. "
        "Jika ditanya berita atau info terkini, jelaskan berdasarkan pengetahuanmu "
        "dan ingatkan bahwa data mungkin tidak real-time."
    )

    history = st.session_state["chat_history"]

    # Render chat bubbles
    with st.container():
        if not history:
            st.markdown("""
            <div class="empty-state">
                <div class="icon">📰</div>
                <h3>Mulai Bertanya</h3>
                <p>Ketik pertanyaanmu di bawah untuk mulai percakapan.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            for msg in history:
                with st.chat_message(msg["role"],
                                     avatar="⚡" if msg["role"] == "assistant" else "👤"):
                    st.markdown(msg["content"])
                    st.markdown(
                        f'<div style="font-size:10px;color:#444;margin-top:4px">'
                        f'{msg.get("time","")}</div>',
                        unsafe_allow_html=True
                    )

    # Chat input
    if prompt := st.chat_input("Tanya sesuatu...", key="chat_input_info"):
        # Append user msg
        st.session_state["chat_history"].append({
            "role": "user",
            "content": prompt,
            "time": now_str()
        })
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Build context (last 10 exchanges)
        ctx_msgs = history[-20:]
        context = "\n".join(
            f"{'User' if m['role']=='user' else 'ICANG'}: {m['content']}"
            for m in ctx_msgs
        )
        full_prompt = f"{SYSTEM}\n\nRiwayat percakapan:\n{context}\n\nUser: {prompt}\nICANG:"

        # Stream AI response
        with st.chat_message("assistant", avatar="⚡"):
            with st.spinner(""):
                reply = ask_ai(full_prompt)
            st.markdown(reply)
            st.markdown(
                f'<div style="font-size:10px;color:#444;margin-top:4px">{now_str()}</div>',
                unsafe_allow_html=True
            )

        st.session_state["chat_history"].append({
            "role": "assistant",
            "content": reply,
            "time": now_str()
        })
        st.rerun()


# ─────────────────────────────────────────
# PAGE: BUAT CERITA (chat style)
# ─────────────────────────────────────────
def page_cerita():
    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">📝</div>
        <div>
            <div class="page-header-title">Buat Cerita</div>
            <div class="page-header-sub">Ceritakan idemu — AI akan menuliskan ceritanya</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    SYSTEM = (
        "Kamu adalah penulis kreatif berbahasa Indonesia. "
        "Buat cerita pendek yang menarik, mengalir, dan imajinatif "
        "berdasarkan prompt yang diberikan user. "
        "Gunakan narasi yang hidup dan deskripsi yang vivid. "
        "Panjang cerita sekitar 3-5 paragraf kecuali diminta berbeda."
    )

    history = st.session_state["cerita_history"]

    if not history:
        st.markdown("""
        <div class="empty-state">
            <div class="icon">📝</div>
            <h3>Buat Cerita Pertamamu</h3>
            <p>Deskripsikan ide ceritamu, dan AI akan menuliskannya untukmu.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in history:
            with st.chat_message(msg["role"],
                                 avatar="⚡" if msg["role"] == "assistant" else "👤"):
                st.markdown(msg["content"])
                st.markdown(
                    f'<div style="font-size:10px;color:#444;margin-top:4px">'
                    f'{msg.get("time","")}</div>',
                    unsafe_allow_html=True
                )

    if prompt := st.chat_input("Ceritakan idemu... (contoh: petualangan di hutan mistis)", key="chat_cerita"):
        st.session_state["cerita_history"].append({
            "role": "user",
            "content": prompt,
            "time": now_str()
        })
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        ctx_msgs = history[-10:]
        context = "\n".join(
            f"{'User' if m['role']=='user' else 'ICANG'}: {m['content'][:300]}"
            for m in ctx_msgs
        )
        full_prompt = (
            f"{SYSTEM}\n\nKonteks sebelumnya:\n{context}\n\n"
            f"User minta: {prompt}\nTulis ceritanya:"
        )

        with st.chat_message("assistant", avatar="⚡"):
            with st.spinner("Menulis cerita..."):
                reply = ask_ai(full_prompt)
            st.markdown(reply)
            st.markdown(
                f'<div style="font-size:10px;color:#444;margin-top:4px">{now_str()}</div>',
                unsafe_allow_html=True
            )

        st.session_state["cerita_history"].append({
            "role": "assistant",
            "content": reply,
            "time": now_str()
        })
        st.rerun()


# ─────────────────────────────────────────
# PAGE: HITUNG MATEMATIKA (chat style)
# ─────────────────────────────────────────
def page_matematika():
    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">🧮</div>
        <div>
            <div class="page-header-title">Hitung Matematika</div>
            <div class="page-header-sub">Soal matematika, fisika, statistik — tanya langsung</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    SYSTEM = (
        "Kamu adalah tutor matematika dan sains berbahasa Indonesia. "
        "Jawab soal dengan langkah-langkah yang jelas dan terstruktur. "
        "Gunakan format: "
        "1. Identifikasi masalah, "
        "2. Rumus yang digunakan, "
        "3. Langkah pengerjaan step-by-step, "
        "4. Hasil akhir. "
        "Jika perlu, gunakan notasi matematis yang mudah dibaca dalam teks biasa."
    )

    history = st.session_state["math_history"]

    if not history:
        st.markdown("""
        <div class="empty-state">
            <div class="icon">🧮</div>
            <h3>Tanya Soal Matematika</h3>
            <p>Ketik soal atau pertanyaan matematikamu di bawah.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in history:
            with st.chat_message(msg["role"],
                                 avatar="⚡" if msg["role"] == "assistant" else "👤"):
                st.markdown(msg["content"])
                st.markdown(
                    f'<div style="font-size:10px;color:#444;margin-top:4px">'
                    f'{msg.get("time","")}</div>',
                    unsafe_allow_html=True
                )

    if prompt := st.chat_input("Ketik soal matematikamu...", key="chat_math"):
        st.session_state["math_history"].append({
            "role": "user",
            "content": prompt,
            "time": now_str()
        })
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        ctx_msgs = history[-10:]
        context = "\n".join(
            f"{'User' if m['role']=='user' else 'ICANG'}: {m['content'][:200]}"
            for m in ctx_msgs
        )
        full_prompt = (
            f"{SYSTEM}\n\nRiwayat:\n{context}\n\n"
            f"Soal baru: {prompt}\nJawaban:"
        )

        with st.chat_message("assistant", avatar="⚡"):
            with st.spinner("Menghitung..."):
                reply = ask_ai(full_prompt)
            st.markdown(reply)
            st.markdown(
                f'<div style="font-size:10px;color:#444;margin-top:4px">{now_str()}</div>',
                unsafe_allow_html=True
            )

        st.session_state["math_history"].append({
            "role": "assistant",
            "content": reply,
            "time": now_str()
        })
        st.rerun()


# ─────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────
halaman = st.session_state.get("halaman", "info")

if halaman == "info":
    page_info()
elif halaman == "cerita":
    page_cerita()
elif halaman == "matematika":
    page_matematika()
