import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime

# ─────────────────────────────
# INIT
# ─────────────────────────────
load_dotenv()

st.set_page_config(
    page_title="ICANG AI SEARCH",
    page_icon="⚡",
    layout="centered"
)

# ─────────────────────────────
# AI SETUP (NEW MODEL)
# ─────────────────────────────
@st.cache_resource
def init_model():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("API KEY tidak ditemukan di .env")
        st.stop()

    genai.configure(api_key=api_key)

    # Model terbaru (lebih pintar & stabil)
    return genai.GenerativeModel("gemini-2.5-pro")

model = init_model()


# ─────────────────────────────
# FUNCTION AI CALL
# ─────────────────────────────
def ask_ai(prompt):
    try:
        res = model.generate_content(prompt)
        return res.text
    except Exception as e:
        return f"Error: {str(e)}"


def now():
    return datetime.now().strftime("%H:%M")


# ─────────────────────────────
# SESSION
# ─────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []


# ─────────────────────────────
# UI HEADER
# ─────────────────────────────
st.markdown("""
# ⚡ ICANG AI SEARCH
**Satu kolom pencarian untuk semua jawaban**
---
""")


# ─────────────────────────────
# SEARCH INPUT
# ─────────────────────────────
query = st.text_input("Tanyakan apa saja...", placeholder="Contoh: jelaskan black hole, atau hitung 25x12")

SYSTEM = """
Kamu adalah AI assistant modern.
Jawab dengan:
- jelas
- ringkas
- akurat
- bahasa Indonesia
Jika pertanyaan kompleks, jelaskan step-by-step.
"""


# ─────────────────────────────
# PROCESS
# ─────────────────────────────
if st.button("Search ⚡") and query:

    st.session_state.history.append(("user", query, now()))

    full_prompt = f"{SYSTEM}\n\nUser: {query}\nJawaban:"

    with st.spinner("Mencari jawaban..."):
        answer = ask_ai(full_prompt)

    st.session_state.history.append(("ai", answer, now()))


# ─────────────────────────────
# OUTPUT HISTORY
# ─────────────────────────────
for role, msg, t in st.session_state.history[::-1]:

    if role == "user":
        st.markdown(f"""
        <div style="background:#1a1a1a;padding:10px 14px;
        border-radius:10px;margin:8px 0;color:#fff">
        👤 {msg}
        <div style="font-size:10px;color:#666">{t}</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style="background:#141414;padding:12px 14px;
        border-radius:10px;margin:8px 0;border:1px solid #333">
        ⚡ {msg}
        <div style="font-size:10px;color:#666">{t}</div>
        </div>
        """, unsafe_allow_html=True)
