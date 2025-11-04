import streamlit as st
import requests
st.set_page_config(page_title="Mushaf Digital Quran",page_icon="🕋")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri&display=swap');

    /* Main background */
    body, .css-18e3th9, .stApp {
        font-family: 'Amiri', serif;
        background: linear-gradient(to bottom, #e0f7fa, #ffffff); /* soft turquoise to white */
        color: #064420; /* dark green text */
    }

    /* Sidebar styling - contrasting color */
    .css-1d391kg {
        background-color: #004d40; /* deep teal */
        color: #ffffff; /* white text */
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #00251a;
    }

    /* Headings in sidebar */
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg h5, .css-1d391kg h6 {
        color: #ffd700; /* golden headings */
    }

    /* App title and headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Amiri', serif;
        color: #a67c00; /* golden main headings */
    }

    /* Audio player styling */
    audio {
        width: 100%;
        margin: 5px 0 15px 0;
    }

    /* Surah select box cursor */
    .stSelectbox>div>div>div>div {
        cursor: pointer;
    }

    </style>
""", unsafe_allow_html=True)

st.title("🕋 Mushaf Digital Quran")
st.sidebar.title("📖 Surah Selection")

response = requests.get("https://api.alquran.cloud/v1/surah")
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
    f"https://api.alquran.cloud/v1/surah/{surah_num}/{reciter}"
).json()["data"]["ayahs"]


for ayah in response_surah_audio:
    st.markdown(f"<p style='font-size:22px;'>{ayah['text']}</p>", unsafe_allow_html=True)

    # st.write(ayah["text"])

    st.audio(ayah["audio"])
    
    
    

















