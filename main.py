import streamlit as st
import requests

st.set_page_config(
    page_title="Mushaf Digital Quran",
    page_icon="🕋",
    layout="centered",
)

st.markdown("""
<style>
/* Google Fonts, background, sidebar, etc. */

/* Finger cursor for selectboxes */
[data-baseweb="select"] > div {
    cursor: pointer !important;
}

/* Finger cursor for buttons */
.stButton>button {
    cursor: pointer !important;
}

/* Arabic & English text styling etc. */
</style>
""", unsafe_allow_html=True)
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

