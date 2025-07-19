import streamlit as st
import json

# Carrega o conteúdo do JSON (corrigido com subpasta data/)
with open("data/conteudo_semana.json", "r", encoding="utf-8") as f:
    conteudo = json.load(f)

# Configuração da página
st.set_page_config(page_title="Jovem Conectado - IASD", layout="wide")

# Menu lateral (sidebar)
menu = st.sidebar.selectbox("📚 Selecione uma seção", [
    "Versículo da Semana",
    "Devocional",
    "Desafio Espiritual",
    "Personagem Bíblico",
    "Frase Motivacional",
    "Reflexão",
    "Vida Profissional",
    "Esboço Técnico"
])

# Função auxiliar para texto justificado
def justificado(texto):
    return f"<p style='text-align: justify;'>{texto}</p>"

# 1. Versículo da Semana
if menu == "Versículo da Semana":
    st.title("📖 Versículo da Semana")
    st.markdown(justificado(f"<em>\"{conteudo['versiculo']['texto']}\"</em><br><strong>📍 {conteudo['versiculo']['referencia']}</strong>"), unsafe_allow_html=True)

# 2. Devocional
elif menu == "Devocional":
    st.title("🙏 Devocional da Semana")
    st.subheader(conteudo['devocional']['titulo'])
    st.markdown(justificado(conteudo['devocional']['texto']), unsafe_allow_html=True)

# 3. Desafio Espiritual
elif menu == "Desafio Espiritual":
    st.title("🧎 Desafio Espiritual")
    st.markdown(justificado(conteudo['desafio_espiritual']), unsafe_allow_html=True)

# 4. Personagem Bíblico
elif menu == "Personagem Bíblico":
    st.title(f"🧔‍♂️ Personagem: {conteudo['personagem']['nome']}")
    st.subheader("✅ Qualidades")
    st.markdown(justificado(conteudo['personagem']['qualidades']), unsafe_allow_html=True)
    st.subheader("⚠️ Fraquezas")
    st.markdown(justificado(conteudo['personagem']['fraquezas']), unsafe_allow_html=True)
    st.subheader("📌 Lição para hoje")
    st.markdown(f"<div style='background-color: #eaf4ff; padding: 10px; border-radius: 8px;'>{conteudo['personagem']['lição']}</div>", unsafe_allow_html=True)

# 5. Frase Motivacional
elif menu == "Frase Motivacional":
    st.title("💬 Frase Motivacional")
    st.markdown(justificado(f"<em>{conteudo['motivacional']['frase']}</em>"), unsafe_allow_html=True)

# 6. Reflexão
elif menu == "Reflexão":
    st.title("🤔 Reflexão da Semana")
    st.markdown(justificado(conteudo['reflexao']), unsafe_allow_html=True)

# 7. Vida Profissional
elif menu == "Vida Profissional":
    st.title("💼 Vida Profissional")
    st.markdown(justificado(f"<strong>Versículo:</strong> <em>\"{conteudo['profissional']['versiculo_texto']}\"</em><br><strong>📍 {conteudo['profissional']['versiculo_ref']}</strong>"), unsafe_allow_html=True)
    st.markdown(justificado(f"<strong>Dica:</strong> {conteudo['profissional']['dica']}"), unsafe_allow_html=True)
    st.markdown(justificado(f"<strong>Desafio:</strong> {conteudo['profissional']['desafio']}"), unsafe_allow_html=True)

# 8. Esboço Técnico
elif menu == "Esboço Técnico":
    st.title("📑 Esboço Técnico — Lição")
    for topico in conteudo["esboco"]["topicos"]:
        st.markdown(f"🔸 {topico}")
