import streamlit as st
import json

# Caminho corrigido para o arquivo JSON
with open("data/conteudo_semana.json", "r", encoding="utf-8") as f:
    conteudo = json.load(f)

st.set_page_config(page_title="Jovem Conectado - IASD", layout="wide")

st.title("📖 Lição da Semana")
st.markdown(f"<p style='text-align: justify;'><strong><u>Versículo:</u></strong> <br><em>\"{conteudo['versiculo']['texto']}\"</em><br>📍 <strong>{conteudo['versiculo']['referencia']}</strong></p>", unsafe_allow_html=True)

st.header("🙏 Devocional da Semana")
st.markdown(f"<h4>{conteudo['devocional']['titulo']}</h4>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: justify;'>{conteudo['devocional']['texto']}</p>", unsafe_allow_html=True)

st.header("📌 Desafio Espiritual")
st.markdown(f"<p style='text-align: justify;'>{conteudo['desafio_espiritual']}</p>", unsafe_allow_html=True)

st.header("🧔‍♂️ Personagem: " + conteudo['personagem']['nome'])
st.subheader("✅ Qualidades")
st.markdown(f"<p style='text-align: justify;'>{conteudo['personagem']['qualidades']}</p>", unsafe_allow_html=True)
st.subheader("⚠️ Fraquezas")
st.markdown(f"<p style='text-align: justify;'>{conteudo['personagem']['fraquezas']}</p>", unsafe_allow_html=True)
st.subheader("📌 Lição para hoje")
st.markdown(f"<div style='background-color: #eaf4ff; padding: 10px; border-radius: 8px; text-align: justify;'>{conteudo['personagem']['lição']}</div>", unsafe_allow_html=True)

st.header("💬 Frase Motivacional")
st.markdown(f"<p style='text-align: justify;'><em>{conteudo['motivacional']['frase']}</em></p>", unsafe_allow_html=True)

st.header("🤔 Reflexão da Semana")
st.markdown(f"<p style='text-align: justify;'>{conteudo['reflexao']}</p>", unsafe_allow_html=True)

st.header("💼 Vida Profissional")
st.markdown(f"<strong>Versículo:</strong> <br><em>\"{conteudo['profissional']['versiculo_texto']}\"</em><br>📍 <strong>{conteudo['profissional']['versiculo_ref']}</strong>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: justify;'><strong>Dica:</strong> {conteudo['profissional']['dica']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: justify;'><strong>Desafio:</strong> {conteudo['profissional']['desafio']}</p>", unsafe_allow_html=True)

st.header("📑 Esboço Técnico")
for topico in conteudo["esboco"]["topicos"]:
    st.markdown(f"- {topico}")
