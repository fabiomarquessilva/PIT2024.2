import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Configuração inicial da página
st.set_page_config(
    page_title="Gerador de PIT Docente",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cabeçalho Institucional
st.markdown("""
<div style="text-align: center;">
    <h2>UNIVERSIDADE FEDERAL DE CAMPINA GRANDE</h2>
    <h3>CENTRO DE FORMAÇÃO DE PROFESSORES</h3>
    <h4>UNIDADE ACADÊMICA DE ENFERMAGEM</h4>
    <br>
    <h3>PLANO INDIVIDUAL DE TRABALHO DOCENTE (PIT)</h3>
</div>
""", unsafe_allow_html=True)

st.write("### Preencha os dados abaixo para gerar seu relatório.")

# Coletar Informações Pessoais
st.subheader("Informações do Docente")
nome = st.text_input("Nome do Docente", placeholder="Digite o nome completo")
siape = st.text_input("Matrícula SIAPE", placeholder="Digite a matrícula SIAPE")
unidade = st.text_input("Unidade Acadêmica", placeholder="Digite a unidade acadêmica")
periodo = st.text_input("Período Letivo", placeholder="Exemplo: 2024.2")

# Coletar Atividades
st.subheader("Atividades de Ensino")
atividades_ensino = st.text_area(
    "Atividades de Ensino e Carga Horária",
    placeholder="Exemplo:\nFARMACOLOGIA: 4 horas/semana\nHISTOLOGIA I: 2 horas/semana"
)

st.subheader("Atividades de Pesquisa")
atividades_pesquisa = st.text_area(
    "Atividades de Pesquisa e Carga Horária",
    placeholder="Exemplo:\nIMUNIDADE PROLONGADA: 4 horas/semana"
)

st.subheader("Atividades de Extensão")
atividades_extensao = st.text_area(
    "Atividades de Extensão e Carga Horária",
    placeholder="Exemplo:\nORIENTAÇÃO SOBRE PREVENÇÃO ÀS ISTs: 6 horas/semana"
)

st.subheader("Atividades Administrativas")
atividades_administrativas = st.text_area(
    "Atividades Administrativas e Carga Horária",
    placeholder="Exemplo:\nMEMBRO DE ASSEMBLEIA ACADÊMICA: 1 hora/semana"
)

st.subheader("Produção Intelectual")
atividades_producao = st.text_area(
    "Produções Intelectuais e Carga Horária",
    placeholder="Exemplo:\nINVESTIGAÇÃO DA LONGEVIDADE DE ANTICORPOS: 3 horas/semana"
)

# Botão para gerar o PDF
if st.button("Gerar Relatório em PDF"):
    # Gerar o PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    pdf.drawString(100, 750, "PLANO INDIVIDUAL DE TRABALHO DOCENTE (PIT)")
    pdf.drawString(100, 730, f"Docente: {nome}")
    pdf.drawString(100, 710, f"Matrícula SIAPE: {siape}")
    pdf.drawString(100, 690, f"Unidade Acadêmica: {unidade}")
    pdf.drawString(100, 670, f"Período Letivo: {periodo}")

    def adicionar_atividades(titulo, atividades, y):
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(100, y, titulo)
        pdf.setFont("Helvetica", 12)
        y -= 20
        for linha in atividades.strip().split("\n"):
            pdf.drawString(100, y, linha)
            y -= 20
        return y - 10

    y = 650
    y = adicionar_atividades("Atividades de Ensino", atividades_ensino, y)
    y = adicionar_atividades("Atividades de Pesquisa", atividades_pesquisa, y)
    y = adicionar_atividades("Atividades de Extensão", atividades_extensao, y)
    y = adicionar_atividades("Atividades Administrativas", atividades_administrativas, y)
    y = adicionar_atividades("Produção Intelectual", atividades_producao, y)

    pdf.save()
    buffer.seek(0)

    # Baixar o PDF
    st.download_button(
        label="Baixar Relatório",
        data=buffer,
        file_name="Relatorio_PIT.pdf",
        mime="application/pdf"
    )
