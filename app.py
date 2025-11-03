import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

@st.cache_resource
def init_google_ai():
    try:
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("⚠ Google API Key tidak ditemukan! Silakan tambahkan ke file .env")
            st.stop()
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        st.error(f"❌ Error saat menginisialisasi Google AI: {str(e)}")
        st.stop()

def run():
    st.set_page_config(
        page_title="Icang AI",
        page_icon="🚀"
    )

    with st.sidebar:
        st.title("📂 Navigasi")
        st.divider()
        st.write("Pilih halaman:")

        # Gunakan key yang konsisten
        if st.button("📰 Cari Berita"):
            st.session_state["halaman"] = "info"

        if st.button("📝 Buat Cerita"):
            st.session_state["halaman"] = "cerita"

        if st.button("🧮 Hitung Matematika"):
            st.session_state["halaman"] = "matematika"

        st.divider()

    # Inisialisasi Google AI sekali saja
    model = init_google_ai()

    # Routing manual
    halaman = st.session_state.get("halaman", "info")

    if halaman == "info":
        from pages.info import run_info
        run_info()
    elif halaman == "cerita":
        from pages.info import run_cerita
        run_cerita()
    elif halaman == "matematika":
        from pages.matematika import run_matematika
        run_matematika()

    st.divider()

if __name__ == "__main__":
    run()
