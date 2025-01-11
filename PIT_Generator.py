import streamlit as st
from fpdf import FPDF
from io import BytesIO

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
    # Criar o PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="PLANO INDIVIDUAL DE TRABALHO DOCENTE (PIT)", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Docente: {nome}", ln=True)
    pdf.cell(200, 10, txt=f"Matrícula SIAPE: {siape}", ln=True)
    pdf.cell(200, 10, txt=f"Unidade Acadêmica: {unidade}", ln=True)
    pdf.cell(200, 10, txt=f"Período Letivo: {periodo}", ln=True)
    pdf.ln(10)

    def adicionar_atividades(titulo, atividades):
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt=titulo, ln=True)
        pdf.set_font("Arial", size=12)
        for linha in atividades.strip().split("\n"):
            pdf.cell(200, 10, txt=linha, ln=True)
        pdf.ln(5)

    adicionar_atividades("Atividades de Ensino", atividades_ensino)
    adicionar_atividades("Atividades de Pesquisa", atividades_pesquisa)
    adicionar_atividades("Atividades de Extensão", atividades_extensao)
    adicionar_atividades("Atividades Administrativas", atividades_administrativas)
    adicionar_atividades("Produção Intelectual", atividades_producao)

    # Salvar o PDF em memória
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    # Botão para download
    st.download_button(
        label="Baixar Relatório",
        data=pdf_buffer,
        file_name="Relatorio_PIT.pdf",
        mime="application/pdf"
    )
