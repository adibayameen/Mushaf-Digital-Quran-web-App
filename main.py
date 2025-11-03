import streamlit as st
import requests

st.set_page_config(
    page_title="Mushaf Digital Quran",
    page_icon="🕋",
    layout="centered",
)

st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Amiri&family=Poppins:wght@400;600&display=swap');

    /* App background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom right, #eef2f3, #dfe9f3);
    }

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }

    /* General text (English) */
    * {
        font-family: 'Poppins', sans-serif;
        color: #333333;
    }

    /* Title */
    h1 {
        font-family: 'Poppins', sans-serif;
        color: #004d40;
        text-align: center;
        font-weight: 600;
    }

    /* Sidebar text */
    [data-testid="stSidebar"] * {
        font-family: 'Poppins', sans-serif;
        color: #222;
    }

    /* ✅ Add pointer cursor for dropdowns */
    select, .stSelectbox, [data-baseweb="select"] {
        cursor: pointer !important;
    }

    /* ✅ Add pointer for buttons too */
    button, .stButton>button {
        cursor: pointer !important;
    }

    /* Quran Arabic text */
    .quran-text {
        font-family: 'Amiri', serif;
        font-size: 24px;
        direction: rtl;
        text-align: right;
        line-height: 2.3;
        color: #1b1b1b;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Section separators */
    hr {
        border: 0;
        height: 1px;
        background: #ccc;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- App Logic --------------------
st.title("🕋 Mushaf Digital Quran")
st.sidebar.title("📖 Surah Selection")

response = requests.get("http://api.alquran.cloud/v1/surah")
response_Surah = response.json()["data"]

Arabic_Surah_Name = [f"{s['number']}. {s['englishName']} {s['name']}" for s in response_Surah]
Selected_Surah_Name = st.sidebar.selectbox("📜 Choose Surah", Arabic_Surah_Name)
surah_num = int(Selected_Surah_Name.split(".")[0])

reciters = [
    "ar.abdurrahmaansudais",
    "ar.saoodshuraym",
    "ar.mahermuaiqly",
    "ar.alafasy"
]
reciter = st.sidebar.selectbox("🎧 Choose Reciter", reciters)

response_surah_audio = requests.get(
    f"http://api.alquran.cloud/v1/surah/{surah_num}/{reciter}"
).json()["data"]["ayahs"]

for ayah in response_surah_audio:
    st.markdown(f'<div class="quran-text">{ayah["text"]}</div>', unsafe_allow_html=True)
    st.audio(ayah["audio"])
