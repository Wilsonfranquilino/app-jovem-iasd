import streamlit as st
import json
from PIL import Image
import os

st.set_page_config(page_title="Conectados na Lição - IASD Distrito Mantena", layout="wide")

# Carregar conteúdo do JSON
with open("data/conteudo_semana.json", "r", encoding="utf-8") as file:
    conteudo = json.load(file)

# Título principal
st.title("🙌 Conectados na Lição - IASD Distrito Mantena")

# Menu lateral para navegação
page = st.sidebar.radio(
    "📄 Menu de Navegação",
    ["Lição em PDF", "Fé e Inspiração", "Personagem da Semana", "Motivação e Reflexão", "Vida Profissional"]
)

# --- Lição em PDF ---
if page == "Lição em PDF":
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

    # 👇 Esboço Técnico
    st.header("🗒️ Esboço Técnico da Lição")
    st.markdown("""
    ## ✨ **Esboço Técnico — Lição 1: Êxodo, A Jornada do Povo de Deus**

    ### 📌 1. Introdução ao livro de Êxodo
    - Segunda parte do Pentateuco (Torá).
    - "Êxodo" vem do grego *Exodos* = "saída" ou "caminho para fora" (Êx 1:1-7).
    - Continuação direta do final de Gênesis (Gn 46–50).

    ### 🏺 2. Contexto histórico
    - Descida da família de José ao Egito (Gn 46).
    - Crescimento e multiplicação do povo (Êx 1:7).
    - Surgimento de novo faraó que não conhecia José (Êx 1:8).

    ### 👑 3. Opressão dos hebreus
    - Escravização e trabalhos forçados (Êx 1:11-14).
    - Decreto de morte para os meninos hebreus (Êx 1:15-22).

    ### 🧑‍🍼 4. As parteiras Sifrá e Puá
    - Resistiram ao faraó e salvaram os bebês (Êx 1:15-21).

    ### 👶 5. Nascimento de Moisés
    - Escondido por três meses (Êx 2:1-2).
    - Colocado no cesto no Nilo (Êx 2:3-4).
    - Encontrado e adotado pela filha do faraó (Êx 2:5-10).

    ### 🏺 6. Significado do nome Moisés
    - "Moisés" significa "tirado das águas" (Êx 2:10).

    ### 🗺️ 7. Moisés no palácio
    - Criado como príncipe no Egito (At 7:22).
    - Educação egípcia estratégica para liderança futura.

    ### 💬 8. Deus ouve o clamor do povo
    - Deus vê a aflição (Êx 2:23-25).
    - Lembra da aliança com Abraão, Isaque e Jacó (Êx 2:24).

    ### 🛡️ 9. O Deus do Êxodo
    - Deus compassivo, gracioso, paciente, cheio de amor e fidelidade (Êx 34:6-7).
    - Libertador e guia do povo.

    ### ⚔️ 10. Faraós mencionados indiretamente
    - Nenhum faraó nomeado no texto.
    - Possíveis identificações históricas:
      - Faraó da opressão: Amenófis I.
      - Faraó do decreto de morte: Tutmés I.
      - Faraó do Êxodo: Tutmés III.

    ### 📄 Resumo final
    - Êxodo marca o nascimento da nação israelita.
    - Preservação de Moisés como líder.
    - Ênfase na fidelidade de Deus à aliança.
    """)

# --- Fé e Inspiração ---
elif page == "Fé e Inspiração":
    st.header("📖 Versículo da Semana")
    st.markdown(f"**{conteudo['versiculo']['referencia']}**")
    st.success(conteudo['versiculo']['texto'])

    st.header("🙏 Devocional")
    st.subheader(conteudo['devocional']['titulo'])
    st.write(conteudo['devocional']['texto'])

    st.header("🎯 Desafio Espiritual")
    st.info(conteudo['desafio_espiritual'])

# --- Personagem da Semana ---
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

# --- Motivação e Reflexão ---
elif page == "Motivação e Reflexão":
    st.header("💬 Frase Motivacional")
    st.success(conteudo['motivacional']['frase'])

    st.header("📌 Reflexão para o dia a dia")
    st.write(conteudo['reflexao'])

# --- Vida Profissional ---
elif page == "Vida Profissional":
    st.header("🚀 Dica Profissional")
    st.write(conteudo['profissional']['dica'])

    st.header("📖 Versículo aplicado à carreira")
    st.markdown(f"**{conteudo['profissional']['versiculo_ref']}**")
    st.info(conteudo['profissional']['versiculo_texto'])

    st.header("🎯 Mini Desafio")
    st.warning(conteudo['profissional']['desafio'])
