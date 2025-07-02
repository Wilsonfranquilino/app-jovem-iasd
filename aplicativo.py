import streamlit as st
import json
from PIL import Image
import os

st.set_page_config(page_title="Conectados na Lição - IASD Distrito Mantena", layout="wide")

# Load weekly content
with open("data/conteudo_semana.json", "r", encoding="utf-8") as file:
    conteudo = json.load(file)

# App title and layout
st.title("🙌 Conectados na Lição - IASD Distrito Mantena")

# Tabs (Abas)
tab0, tab1, tab2, tab3, tab4 = st.tabs(["Lição Completa (PDF)", "Fé e Inspiração", "Personagem da Semana", "Motivação", "Vida Profissional"])

# --- Aba 0: Lição Completa ---
with tab0:
    st.header("📄 Lição Completa da Semana")
    st.info(
        "⚡ **Atenção!**\n\n"
        "Para melhor leitura e experiência, recomendamos baixar o PDF da lição completa da semana. "
        "Assim você poderá ler com calma, marcar anotações e ter sempre à mão, mesmo sem internet. "
        "Clique no botão **📥 Baixar Lição em PDF** abaixo para baixar agora mesmo!"
    )

    pdf_path = "pdf/licao_semana.pdf"

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Baixar Lição em PDF",
                data=f,
                file_name="licao_semana.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Arquivo da lição não encontrado. Por favor, envie o PDF para a pasta correta.")

# --- Aba 1: Fé e Inspiração ---
with tab1:
    st.header("📖 Versículo da Semana")
    st.markdown(f"**{conteudo['versiculo']['referencia']}**")
    st.success(conteudo['versiculo']['texto'])

    st.header("🙏 Devocional")
    st.subheader(conteudo['devocional']['titulo'])
    st.write(conteudo['devocional']['texto'])

    st.header("🎯 Desafio Espiritual")
    st.info(conteudo['desafio_espiritual'])

# --- Aba 2: Personagem Bíblico ---
with tab2:
    st.header(f"🧍 Personagem da Semana: {conteudo['personagem']['nome']}")

    img_path = f"img/{conteudo['personagem']['nome'].lower()}.png"
    if os.path.exists(img_path):
        st.image(Image.open(img_path), width=300)

    st.subheader("✅ Qualidades")
    st.write(conteudo['personagem']['qualidades'])

    st.subheader("⚠️ Fraquezas")
    st.write(conteudo['personagem']['fraquezas'])

    st.subheader("📌 Lição para hoje")
    st.info(conteudo['personagem']['lição'])

# --- Aba 3: Motivação e Vida Real ---
with tab3:
    st.header("💬 Frase Motivacional da Semana")
    st.success(conteudo['motivacional']['frase'])

    st.header("📌 Reflexão para o dia a dia")
    st.write(conteudo['reflexao'])

# --- Aba 4: Vida Profissional e Propósito ---
with tab4:
    st.header("🚀 Dica Profissional da Semana")
    st.write(conteudo['profissional']['dica'])

    st.header("📖 Versículo aplicado à carreira")
    st.markdown(f"**{conteudo['profissional']['versiculo_ref']}**")
    st.info(conteudo['profissional']['versiculo_texto'])

    st.header("🎯 Mini Desafio")
    st.warning(conteudo['profissional']['desafio'])
