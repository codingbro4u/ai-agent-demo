import streamlit as st

st.set_page_config(
    page_title="HelloFresh AI-Agent",
    page_icon="🥬",
    layout="centered"
)

# Stil: HelloFresh Farben
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    .main {
        background-color: #e8f5e9;
        padding: 2rem;
        border-radius: 10px;
    }
    h1 {
        color: #66bb6a;
        text-align: center;
        font-size: 2.5rem;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo oben
st.markdown(
    """
    <div style='text-align: center; margin-bottom: 20px;'>
        <img src='logo.png' width='200'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Titel & Beschreibung
st.markdown("<h1>Dein intelligenter HelloFresh Support-Agent</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <p style='font-size: 1.2rem; text-align: center; color: #2e7d32;'>
        Fragen zu Rezepten, Lieferungen oder Bestellungen? Gib einfach dein Anliegen ein – unser intelligenter Assistent kümmert sich darum.
    </p>
    """,
    unsafe_allow_html=True
)

# Eingabe mit Dummy-Antwort
user_input = st.text_input("Deine Frage")

if user_input:
    antwort = f"Dies ist eine Beispielantwort auf: '{user_input}'"
    st.markdown(f"<p style='color: #1b5e20; font-size: 1.1rem;'>{antwort}</p>", unsafe_allow_html=True)

# Bestellbereich – NEU
st.markdown("---")
st.subheader("🛒 Direktbestellung")

name = st.text_input("Name")
adresse = st.text_input("Lieferadresse")
gericht = st.selectbox(
    "Wähle ein Gericht für nächste Woche:",
    ["Pasta Basilikum", "Thai Curry", "Quinoa Bowl", "Hähnchen Teriyaki", "Veganer Burger"]
)
anzahl = st.number_input("Portionen", min_value=1, max_value=10, step=1)

if st.button("Bestellung abschicken"):
    if name and adresse:
        st.success(f"Bestellung erfolgreich aufgegeben! 🎉\n\n{name}, du erhältst '{gericht}' ({anzahl}x) an '{adresse}'.")
    else:
        st.error("Bitte Name und Adresse eingeben.")
