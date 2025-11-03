import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

@st.cache_resource
def init_google_ai():
    """
    Inisialisasi Google AI dengan cache
    """
    try:
        # Load environment variables
        load_dotenv()
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("⚠ Google API Key tidak ditemukan! Silakan tambahkan ke file .env")
            st.stop()
        
        # Configure Google AI
        genai.configure(api_key=api_key)
        
        # Initialize model
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        st.error(f"❌ Error saat menginisialisasi Google AI: {str(e)}")
        st.stop()

def run():
    """
    Stage 4: Add AI Integration
    Menambahkan integrasi penuh dengan Google Gemini AI
    """
    
    # Konfigurasi halaman
    st.set_page_config(
        page_title="Icang AI",
        page_icon="🚀"
    )
    
    with st.sidebar:
        st.title("📂 Navigasi")
        st.divider()
        st.write("Pilih halaman:")

        # Pakai session_state untuk pindah halaman
        if st.button("📰 Cari Berita"):
            st.session_state["utama"] = "info"

        if st.button("📰 Buat Cerita"):
            st.session_state["halaman"] = "info"

        if st.button("🧮 Hitung Matematika"):
            st.session_state["halaman"] = "matematika"

        st.divider()

    model = init_google_ai()

    # Routing manual
    halaman = st.session_state.get("halaman", "utama")

    if halaman == "utama":
        from pages.info import run_info
        run_info()
    elif halaman == "info":
        from pages.info import run_cerita
        run_cerita()
    elif halaman == "matematika":
        from pages.matematika import run_matematika
        run_matematika()

        st.divider()
            
    # Inisialisasi Google AI
    model = init_google_ai()

if __name__ == "__main__":
    run()





