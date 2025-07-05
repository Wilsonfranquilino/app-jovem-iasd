import streamlit as st
import json
from PIL import Image
import os

st.set_page_config(page_title="Conectados na Lição - IASD Distrito Mantena", layout="wide")

# Carregar conteúdo do JSON
with open("data/conteudo_semana.json", "r", encoding="utf-8") as file:
    conteudo = json.load(file)

st.title("🙌 Conectados na Lição - IASD Distrito Mantena")

# Menu lateral para navegação
page = st.sidebar.radio(
    "📄 Menu de Navegação",
    ["Lição em PDF", "Fé e Inspiração", "Personagem da Semana", "Motivação e Reflexão", "Vida Profissional"]
)

# --- Aba: Lição em PDF ---
if page == "Lição em PDF":
    st.header("📄 Lição Completa da Semana")
    st.info(
        "⚡ **Atenção!**\n\n"
        "Para melhor leitura e experiência, recomendamos baixar o PDF da lição completa da semana. "
        "Assim você poderá ler com calma, marcar anotações e ter sempre à mão, mesmo sem internet."
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

    # Esboço técnico
    st.header("🗒️ Esboço Técnico")
    st.subheader(conteudo["esboco"]["titulo"])
    for topico in conteudo["esboco"]["topicos"]:
        st.write(f"- {topico}")

# --- Aba: Fé e Inspiração ---
elif page == "Fé e Inspiração":
    st.header("📖 Versículo da Semana")
    st.markdown(f"**{conteudo['versiculo']['referencia']}**")
    st.success(conteudo['versiculo']['texto'])

    st.header("🙏 Devocional")
    st.subheader(conteudo['devocional']['titulo'])
    st.write(conteudo['devocional']['texto'])

    st.header("🎯 Desafio Espiritual")
    st.info(conteudo['desafio_espiritual'])

# --- Aba: Personagem da Semana ---
elif page == "Personagem da Semana":
    st.header(f"🧍 Personagem: {conteudo['personagem']['nome']}")

    img_path = f"img/{conteudo['personagem']['nome'].lower()}.png"
    if os.path.exists(img_path):
        st.image(Image.open(img_path), width=300)

    st.subheader("✅ Qualidades")
    st.write(conteudo['personagem']['qualidades'])

    st.subheader("⚠️ Fraquezas")
    st.write(conteudo['personagem']['fraquezas'])

    st.subheader("📌 Lição para hoje")
    st.info(conteudo['personagem']['lição'])

# --- Aba: Motivação e Reflexão ---
elif page == "Motivação e Reflexão":
    st.header("💬 Frase Motivacional")
    st.success(conteudo['motivacional']['frase'])

    st.header("📌 Reflexão para o dia a dia")
    st.write(conteudo['reflexao'])

# --- Aba: Vida Profissional ---
elif page == "Vida Profissional":
    st.header("🚀 Dica Profissional")
    st.write(conteudo['profissional']['dica'])

    st.header("📖 Versículo aplicado à carreira")
    st.markdown(f"**{conteudo['profissional']['versiculo_ref']}**")
    st.info(conteudo['profissional']['versiculo_texto'])

    st.header("🎯 Mini Desafio")
    st.warning(conteudo['profissional']['desafio'])
