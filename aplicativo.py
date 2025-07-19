import streamlit as st
import json

# Configuração inicial
st.set_page_config(layout="wide")

# CSS para justificação de texto
def set_custom_css():
    st.markdown("""
    <style>
    .justificado {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

set_custom_css()

# Leitura do conteúdo
with open("conteudo_semana.json", "r", encoding="utf-8") as f:
    conteudo = json.load(f)

# Abas do aplicativo
abas = st.tabs([
    "📖 Versículo da Semana",
    "🙏 Devocional",
    "🧔‍♂️ Personagem Bíblico",
    "💬 Frase Motivacional",
    "🤔 Reflexão",
    "💼 Vida Profissional",
    "📚 Esboço Técnico"
])

# 1. Versículo da Semana
with abas[0]:
    st.header("📖 Versículo da Semana")
    st.subheader(conteudo["versiculo"]["referencia"])
    st.markdown(f"<div class='justificado'>{conteudo['versiculo']['texto']}</div>", unsafe_allow_html=True)

# 2. Devocional
with abas[1]:
    st.header("🙏 Devocional")
    st.subheader(conteudo["devocional"]["titulo"])
    st.markdown(f"<div class='justificado'>{conteudo['devocional']['texto']}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📌 Desafio Espiritual")
    st.markdown(f"<div class='justificado'>{conteudo['desafio_espiritual']}</div>", unsafe_allow_html=True)

# 3. Personagem Bíblico
with abas[2]:
    st.header("🧔‍♂️ Personagem Bíblico: " + conteudo["personagem"]["nome"])
    
    if "imagem" in conteudo["personagem"]:
        st.image(conteudo["personagem"]["imagem"], caption=conteudo["personagem"]["nome"])

    st.markdown("**Qualidades:** " + conteudo["personagem"]["qualidades"])
    st.markdown("**Fraquezas:** " + conteudo["personagem"]["fraquezas"])
    st.markdown(f"<div class='justificado'><strong>Lição:</strong> {conteudo['personagem']['lição']}</div>", unsafe_allow_html=True)

# 4. Frase Motivacional
with abas[3]:
    st.header("💬 Frase Motivacional")
    st.markdown(f"<div class='justificado'><em>{conteudo['motivacional']['frase']}</em></div>", unsafe_allow_html=True)

# 5. Reflexão
with abas[4]:
    st.header("🤔 Reflexão")
    st.markdown(f"<div class='justificado'>{conteudo['reflexao']}</div>", unsafe_allow_html=True)

# 6. Vida Profissional
with abas[5]:
    st.header("💼 Vida Profissional")
    st.markdown(f"<div class='justificado'>{conteudo['profissional']['dica']}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📖 Versículo")
    st.markdown(f"**{conteudo['profissional']['versiculo_ref']}**")
    st.markdown(f"<div class='justificado'>{conteudo['profissional']['versiculo_texto']}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🎯 Desafio Profissional")
    st.markdown(f"<div class='justificado'>{conteudo['profissional']['desafio']}</div>", unsafe_allow_html=True)

# 7. Esboço Técnico
with abas[6]:
    st.header(conteudo["esboco"]["titulo"])
    for topico in conteudo["esboco"]["topicos"]:
        st.markdown(f"- {topico}")
