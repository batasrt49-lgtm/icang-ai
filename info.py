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
        Buatkan konten yang menarik dan informatif tentang topik: "{topic}"
        
        Format konten:
        1. Judul yang catchy
        2. Pendahuluan singkat
        3. 3-5 poin utama dengan penjelasan
        4. Kesimpulan
        5. Call to action
        
        Konten harus:
        - Mudah dipahami
        - Informatif dan berguna
        - Engaging untuk pembaca
        - Panjang sekitar 200-300 kata
        
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
        page_title="Icang AI",
        page_icon="🚀"
    )
    
    # Judul aplikasi
    st.title("Icang AI 🚀")
    
    # Teks pembuka
    st.write("Ayo beritahu apa yang anda mau")
    
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
    user_topic = st.text_input(
        "📝 Berikan saya arahan:",
        placeholder="Contoh: Tips Belajar Python, Manfaat AI dalam Bisnis, dll."
    )
    
    # Tampilkan topik yang dimasukkan user
    if user_topic:
        st.write(f"*Topik yang akan diproses:* {user_topic}")
    
    # Tombol untuk generate konten
    if st.button("Mulai mencari", type="primary"):
        if not user_topic.strip():
            st.warning("⚠ Mohon masukkan prompt terlebih dahulu!")
        else:
            # Generate konten menggunakan AI
            with st.spinner("🤖 AI sedang bekerja keras..."):
                hasil_konten = generate_content(user_topic, model)
            
            st.subheader("🤖 Hasil Konten:")
            st.info(hasil_konten)

if __name__ == "__main__":
    run()