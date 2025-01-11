from flask import Flask, render_template, request, send_file
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Função para renderizar o formulário
def render_form():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gerador de PIT Docente</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; margin: 0; padding: 0; }
            .container { max-width: 900px; margin: auto; padding: 20px; background: #fff; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); }
            h1, h2, h3 { text-align: center; color: #0056b3; }
            label { font-weight: bold; display: block; margin-top: 10px; }
            input, textarea, button { margin-top: 5px; padding: 10px; width: 100%; border: 1px solid #ccc; border-radius: 5px; }
            button { background-color: #0056b3; color: white; font-weight: bold; cursor: pointer; }
            button:hover { background-color: #003f7d; }
            .section { margin-bottom: 30px; }
            .section-header { margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Gerador de PIT Docente</h1>
            <p style="text-align: center; font-size: 16px;">Preencha todas as informações abaixo para gerar um relatório detalhado do seu Plano Individual de Trabalho Docente (PIT).</p>
            <div class="section">
                <h2 class="section-header">Cabeçalho</h2>
                <p style="text-align: center;">
                    UNIVERSIDADE FEDERAL DE CAMPINA GRANDE<br>
                    CENTRO DE FORMAÇÃO DE PROFESSORES<br>
                    UNIDADE ACADÊMICA DE ENFERMAGEM<br><br>
                    PLANO INDIVIDUAL DE TRABALHO DOCENTE (PIT)<br><br>
                    Eu, professor(a) FRANCISCO FÁBIO MARQUES DA SILVA, matrícula SIAPE nº 1149343, lotado(a) na Unidade Acadêmica de Enfermagem, regime de trabalho T-40/DE, apresento o PIT referente ao período letivo 2024.2 com as seguintes atividades:<br>
                </p>
            </div>
            <form action="/generate" method="post">
                <div class="section">
                    <h2 class="section-header">Informações Pessoais</h2>
                    <label for="nome">Nome do Docente:</label>
                    <input type="text" id="nome" name="nome" placeholder="Digite o nome do docente">

                    <label for="siape">Matrícula SIAPE:</label>
                    <input type="text" id="siape" name="siape" placeholder="Digite a matrícula SIAPE">

                    <label for="unidade">Unidade Acadêmica:</label>
                    <input type="text" id="unidade" name="unidade" placeholder="Digite a unidade acadêmica">

                    <label for="periodo">Período Letivo:</label>
                    <input type="text" id="periodo" name="periodo" placeholder="Digite o período letivo">
                </div>

                <div class="section">
                    <h2 class="section-header">Atividades de Ensino</h2>
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr>
                            <th style="border: 1px solid #ccc; padding: 8px;">Curso</th>
                            <th style="border: 1px solid #ccc; padding: 8px;">Disciplina(s)</th>
                            <th style="border: 1px solid #ccc; padding: 8px;">Carga Horária Semanal</th>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;">Enfermagem</td>
                            <td style="border: 1px solid #ccc; padding: 8px;"><input type="text" name="disciplina1" placeholder="Exemplo: FARMACOLOGIA"></td>
                            <td style="border: 1px solid #ccc; padding: 8px;"><input type="text" name="carga1" placeholder="Exemplo: 04"></td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;">Enfermagem</td>
                            <td style="border: 1px solid #ccc; padding: 8px;"><input type="text" name="disciplina2" placeholder="Exemplo: HISTOLOGIA I"></td>
                            <td style="border: 1px solid #ccc; padding: 8px;"><input type="text" name="carga2" placeholder="Exemplo: 02"></td>
                        </tr>
                        <tr>
                            <td colspan="2" style="border: 1px solid #ccc; padding: 8px; text-align: right;">TOTAL</td>
                            <td style="border: 1px solid #ccc; padding: 8px;"><input type="text" name="total_ensino" placeholder="Soma das cargas horárias"></td>
                        </tr>
                    </table>
                </div>

                <button type="submit">Gerar Relatório em PDF</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/')
def index():
    return render_form()

@app.route('/generate', methods=['POST'])
def generate():
    nome = request.form['nome']
    siape = request.form['siape']
    unidade = request.form['unidade']
    periodo = request.form['periodo']

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 750, f"Docente: {nome}")
    pdf.drawString(100, 730, f"Matrícula SIAPE: {siape}")
    pdf.drawString(100, 710, f"Unidade Acadêmica: {unidade}")
    pdf.drawString(100, 690, f"Período Letivo: {periodo}")
    pdf.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="Relatorio_PIT.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
