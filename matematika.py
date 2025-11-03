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

def generate_content(topic, model):
    """
    Generate konten menggunakan Google Gemini AI
    """
    try:
        prompt = f"""
        Pecahkan soal matematika berikut dengan langkah-langkah yang sistematis.
        Jika soal berbentuk cerita, gunakan pendekatan soal cerita.
        Jika soal menggunakan rumus langsung, gunakan pendekatan rumus.

        Soal:
        "{topic}"
        """
        
        # ✅ hanya kirim prompt ke model
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"❌ Terjadi error saat menghitung : {str(e)}"

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
    
    # Judul aplikasi
    st.title("Icang MATH AI 🚀")
    
    # Teks pembuka
    st.write("Memecahkan soal Matematika anda")
    
    with st.sidebar:
        st.title("ICANG AI")
        st.divider()
        st.write("Pilih AI anda")
        if st.button("📰 Cari berita"):
            st.switch_page("info.py")

        if st.button("📚 Buat Cerita"):
            st.switch_page("app.py")

        if st.button("🧮 Hitung Matematika"):
            st.switch_page("matematika.py")
        st.divider()
            
    # Inisialisasi Google AI
    model = init_google_ai()
    
    st.divider()

    # Input teks dari user
    user_topic = st.text_input("📝 Berikan Soal :")

    # Tombol untuk generate konten
    if st.button("Mulai menghitung", type="primary"):
        if not user_topic.strip():
            st.warning("⚠ Mohon masukkan soal terlebih dahulu!")
        else:
            # Generate konten menggunakan AI
            with st.spinner("🤖 AI sedang bekerja keras..."):
                hasil_konten = generate_content(user_topic, model)
            
            st.subheader("🤖 Hasil menghitung :")
            st.info(hasil_konten)

if __name__ == "__main__":
    run()