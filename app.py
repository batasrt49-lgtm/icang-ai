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
        api_key = st.secrets["GOOGLE_API_KEY"]

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

def generate_content(topic, model, length, genre):
    """
    Generate konten menggunakan Google Gemini AI
    """
    try:
        prompt = f"""
        Buatkan konten cerita yang menarik tentang topik: "{topic}"
        
        Format konten:
        1. Judul yang catchy
        2. Pendahuluan singkat
        3. Sedikit cerita yang menarik
        4. Dengan genre {genre}
        5. harus ada aktor/pemeran
        6. sesekali ada seperti percakapan dan mungkin tulisan seperti suara haaaaa
        
        Konten harus:
        - Mudah dipahami
        - Menghibur bagi semua usia
        - Panjang sekitar {length} kata
        
        Gunakan bahasa Indonesia yang baik dan benar.
        """
        
        # ✅ hanya kirim prompt ke model
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"❌ Terjadi error saat generate konten: {str(e)}"

def run():
    """
    Stage 4: Add AI Integration
    Menambahkan integrasi penuh dengan Google Gemini AI
    """
    
    # Konfigurasi halaman
    st.set_page_config(
        page_title="AI Content Generator",
        page_icon="🚀"
    )
    
    # Judul aplikasi
    st.title("ICANG AI Generator 🚀")
    
    # Teks pembuka
    st.write("Welcome TO AI ICANG!")
    st.write("Aplikasi ini menggunakan Google Gemini AI untuk membuat konten berkualitas.")
    
    with st.sidebar:
        st.write("ICANG AI")
        length = st.slider(
            "Pilih panjang konten",
            min_value=200,
            max_value=500,
            value=100,
            step=10
        )
        genre = st.selectbox("Pilih kategori konten :", ["Horror", "Komedi", "Serius"])

    # Inisialisasi Google AI
    model = init_google_ai()
    
    st.divider()
    
    # Input teks dari user
    user_topic = st.text_input(
        "📝 Masukkan topik konten:",
        placeholder="Contoh: Tips Belajar Python, Manfaat AI dalam Bisnis, dll."
    )
    
    # Tampilkan topik yang dimasukkan user
    if user_topic:
        st.write(f"*Topik yang akan diproses:* {user_topic}")
    
    # Tombol untuk generate konten
    if st.button("🔥 Generate Konten", type="primary"):
        if not user_topic.strip():
            st.warning("⚠ Mohon masukkan topik terlebih dahulu!")
        else:
            # Generate konten menggunakan AI
            with st.spinner("🤖 AI sedang bekerja keras membuat konten untuk Anda..."):
                hasil_konten = generate_content(user_topic, model, length, genre)
            
            st.success("✅ Konten berhasil dibuat!")
            st.subheader("📄 Hasil Konten:")
            st.info(hasil_konten)

if __name__ == "__main__":
    run()