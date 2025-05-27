import streamlit as st

# Seitenkonfiguration
st.set_page_config(
    page_title="KI-Agent für Unternehmen",
    layout="wide",
    page_icon="🤖"
)

# Überschrift und Einleitung
st.markdown("# 🧠 KI-Agent für Unternehmen")
st.markdown("### Lebenslauf-Analyse – Kundenservice – Versicherungssupport")
st.markdown("---")

# Stil-Anpassung (optional)
st.markdown("""
<style>
textarea {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# Eingabebereich in Spalten
col1, col2 = st.columns([1, 2])

with col1:
    modus = st.selectbox("📂 Modus test wählen", [
        "Lebenslauf analysieren",
        "Support-Anfrage",
        "Versicherungskunde"
    ])

with col2:
    eingabe = st.text_area("✍️ Text eingeben", height=200)

# Analyse-Funktionen
def analyze_cv(text):
    keywords = [
        "python", "data", "machine learning", "sales", "customer", "project",
        "leadership", "excel", "communication", "team", "sql", "crm", "presentation", "analysis"
    ]
    score = sum(1 for word in keywords if word in text.lower())
    feedback = "Geeigneter Kandidat ✅" if score >= 3 else "Unzureichende Qualifikationen ❌"
    return f"Score: {score}/15 – {feedback}"

def handle_support_request(message):
    if "lieferung" in message.lower():
        return "📦 Lieferung in 1–3 Werktagen."
    elif "retoure" in message.lower():
        return "↩️ Retoure über Kundenportal anmelden."
    elif "produkt" in message.lower():
        return "🔎 Bitte geben Sie das Produkt an."
    else:
        return "📨 Anfrage wird weitergeleitet."

def handle_insurance_claim(message):
    if "unfall" in message.lower() or "schaden" in message.lower():
        return "📝 Bitte Schadensformular ausfüllen. Ein Sachbearbeiter meldet sich."
    elif "versicherung" in message.lower():
        return "🔐 Welche Versicherung interessiert Sie?"
    else:
        return "📄 Wir analysieren Ihre Anfrage."

# Antwort generieren
if st.button("🚀 Antwort generieren"):
    if eingabe.strip() == "":
        st.warning("⚠️ Bitte Text eingeben.")
    else:
        if modus == "Lebenslauf analysieren":
            result = analyze_cv(eingabe)
        elif modus == "Support-Anfrage":
            result = handle_support_request(eingabe)
        elif modus == "Versicherungskunde":
            result = handle_insurance_claim(eingabe)
        st.success(f"💬 Antwort: {result}")
