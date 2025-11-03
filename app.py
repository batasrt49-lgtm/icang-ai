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
    
    # Judul aplikasi
    st.title("AI MY Kisah Generator 🚀")
    
    # Teks pembuka
    st.write("Anda bisa generate Cerita yang anda mau dengan judul dan genre yang dapat di sesuaikan")
    
    with st.sidebar:
        st.title("📂 Navigasi")
        st.divider()
        st.write("Pilih halaman:")

        # Pakai session_state untuk pindah halaman
        if st.button("📰 Cari Berita"):
            st.session_state["halaman"] = "info"

        if st.button("🧮 Hitung Matematika"):
            st.session_state["halaman"] = "matematika"

        st.divider()

    model = init_google_ai()

    # Routing manual
    halaman = st.session_state.get("halaman", "utama")

    if halaman == "utama":
        st.text_input("📝 Ketik perintah untuk AI di sini:")
        st.info("Gunakan tombol di sidebar untuk pindah halaman.")
    elif halaman == "info":
        from pages.info import run_info
        run_info()
    elif halaman == "matematika":
        from pages.matematika import run_matematika
        run_matematika()

        st.divider()
            
    # Inisialisasi Google AI
    model = init_google_ai()
    
    st.divider()
    
    col1,col2 = st.columns(2)

    with col1:
        length = st.slider(
            "Pilih panjang konten",
            min_value=200,
            max_value=500,
            value=100,
            step=10
        )
    with col2:
        genre = st.selectbox("Pilih AI Generate :", ["Horror", "Komedi", "Serius"])

    # Input teks dari user
    user_topic = st.text_input(
        "📝 Masukkan judul cerita:",
        placeholder="Contoh: Teror pocong merah, Main bareng teman, dll."
    )
    
    # Tombol untuk generate konten
    if st.button("🔥 Generate Konten", type="primary"):
        if not user_topic.strip():
            st.warning("⚠ Mohon masukkan topik terlebih dahulu!")
        else:
            # Generate konten menggunakan AI
            with st.spinner("🤖 AI sedang bekerja keras membuat Cerita untuk Anda..."):
                hasil_konten = generate_content(user_topic, model, length, genre)
            
            st.subheader("🤖 Hasil Cerita :")
            st.info(hasil_konten)

if __name__ == "__main__":
    run()

