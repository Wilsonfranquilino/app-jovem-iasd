import streamlit as st
import json
from PIL import Image
import os

# Carrega conteúdo do JSON
with open("data/conteudo_semana.json", "r", encoding="utf-8") as f:
    conteudo = json.load(f)

# Layout principal
st.set_page_config(page_title="Lição da Semana - Jovem Conectado", layout="wide")

st.title("📖 Lição da Semana")
st.markdown("---")

# Abas principais
abas = st.tabs(["📜 Versículo", "🙏 Devocional", "🌱 Desafio Espiritual", "🧔 Personagem", "💬 Motivacional", "🧠 Reflexão", "💼 Vida Profissional", "🧩 Esboço Técnico"])

# Aba 1 — Versículo
with abas[0]:
    st.subheader("📜 Versículo da Semana")
    st.markdown(f"**{conteudo['versiculo']['referencia']}**")
    st.markdown(f"<p style='text-align: justify'>{conteudo['versiculo']['texto']}</p>", unsafe_allow_html=True)

# Aba 2 — Devocional
with abas[1]:
    st.subheader(f"🙏 {conteudo['devocional']['titulo']}")
    st.markdown(f"<p style='text-align: justify'>{conteudo['devocional']['texto']}</p>", unsafe_allow_html=True)

# Aba 3 — Desafio Espiritual
with abas[2]:
    st.subheader("🌱 Desafio Espiritual")
    st.markdown(f"<p style='text-align: justify'>{conteudo['desafio_espiritual']}</p>", unsafe_allow_html=True)

# Aba 4 — Personagem
with abas[3]:
    st.subheader(f"🧔 Personagem Bíblico: {conteudo['personagem']['nome']}")
    imagem_path = f"imagens/{conteudo['personagem']['nome'].lower()}.png"
    if os.path.exists(imagem_path):
        st.image(imagem_path, width=300)
    st.markdown(f"**Qualidades:** {conteudo['personagem']['qualidades']}")
    st.markdown(f"**Fraquezas:** {conteudo['personagem']['fraquezas']}")
    st.markdown(f"<p style='text-align: justify'><strong>Lição:</strong> {conteudo['personagem']['lição']}</p>", unsafe_allow_html=True)

# Aba 5 — Motivacional
with abas[4]:
    st.subheader("💬 Frase Motivacional")
    st.markdown(f"<p style='text-align: justify'><em>{conteudo['motivacional']['frase']}</em></p>", unsafe_allow_html=True)

# Aba 6 — Reflexão
with abas[5]:
    st.subheader("🧠 Reflexão")
    st.markdown(f"<p style='text-align: justify'>{conteudo['reflexao']}</p>", unsafe_allow_html=True)

# Aba 7 — Vida Profissional
with abas[6]:
    st.subheader("💼 Vida Profissional")
    st.markdown(f"**Dica:** {conteudo['profissional']['dica']}")
    st.markdown(f"📖 {conteudo['profissional']['versiculo_ref']}: *{conteudo['profissional']['versiculo_texto']}*")
    st.markdown(f"**Desafio:** {conteudo['profissional']['desafio']}")

# Aba 8 — Esboço Técnico
with abas[7]:
    st.subheader(conteudo['esboco']['titulo'])
    for item in conteudo['esboco']['topicos']:
        st.markdown(f"- {item}")
