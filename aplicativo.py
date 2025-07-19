import streamlit as st
import json
from PIL import Image
import os

st.set_page_config(page_title="Conectados na Lição - IASD Distrito Mantena", layout="wide")

# Carregar conteúdo do JSON
with open("data/conteudo_semana.json", "r", encoding="utf-8") as file:
    conteudo = json.load(file)

st.title("🙌 Conectados na Lição - IASD Distrito Mantena")

# Aviso para celulares sobre o menu lateral
st.markdown("""
<div style='background-color: #f0f2f6; padding: 10px; border-radius: 8px; font-size: 16px'>
📱 <strong>Para celulares:</strong> Toque no <strong>menu ☰ no canto superior esquerdo</strong> para navegar entre as abas do aplicativo. 👉
</div>
""", unsafe_allow_html=True)

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
    else
