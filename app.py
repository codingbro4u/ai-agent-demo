import streamlit as st

st.set_page_config(page_title="GastroBot", page_icon="🍽️", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f7fff7;
        padding: 2rem;
        border-radius: 10px;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #2e7d32;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>🍽️ GastroBot – Dein digitaler Gastro-Assistent</h1>", unsafe_allow_html=True)

st.markdown("### 🤖 Fragen zum Angebot?")
frage = st.text_input("Was möchtest du wissen?")

if frage:
    st.markdown(f"**Antwort:** Unsere KI bearbeitet: *'{frage}'* – (echte Logik wird hier später ergänzt)")

st.markdown("---")
st.subheader("🛒 Bestellung aufgeben")

name = st.text_input("Dein Name")
gericht = st.selectbox("Wähle dein Gericht:", ["Spaghetti Bolognese", "Pizza Margherita", "Veganes Curry", "Caesar Salad"])
menge = st.number_input("Menge", min_value=1, max_value=20, step=1)
adresse = st.text_input("Lieferadresse")

if st.button("Bestellung absenden"):
    if name and adresse:
        st.success(f"Vielen Dank, {name}! Du erhältst {menge}x {gericht} an {adresse}.")
    else:
        st.error("Bitte gib Name und Adresse ein.")
