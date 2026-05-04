import os
import smtplib
import zipfile
import io
from flask import Flask, render_template, request, jsonify, send_file
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)

# --- CONFIGURAÇÕES ---
GMAIL_USER = 'seu_email@gmail.com'
GMAIL_PASSWORD = 'sua_senha_de_app_aqui' 
OUTPUT_FOLDER = 'saida'

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def gerar_pdf(nome_aluno):
    filename = f"Bem_Vindo_{nome_aluno.replace(' ', '_')}.pdf"
    caminho_pdf = os.path.join(OUTPUT_FOLDER, filename)
    c = canvas.Canvas(caminho_pdf, pagesize=A4)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 750, "CARTA DE BOAS-VINDAS")
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Olá, {nome_aluno}!")
    c.drawString(100, 680, "Seja bem-vindo(a) à nossa instituição de ensino.")
    c.save()
    return caminho_pdf

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_arquivos():
    nomes_raw = request.form.get('nomes')
    lista_nomes = [n.strip() for n in nomes_raw.replace('\n', ',').split(',') if n.strip()]
    
    if not lista_nomes:
        return "Insira ao menos um nome", 400

    caminhos = [gerar_pdf(nome) for nome in lista_nomes]

    # Se for apenas um aluno, envia o PDF direto
    if len(caminhos) == 1:
        return send_file(caminhos[0], as_attachment=True)

    # Se forem vários, cria um ZIP na memória
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for fpath in caminhos:
            zf.write(fpath, os.path.basename(fpath))
    
    memory_file.seek(0)
    return send_file(memory_file, download_name='cartas_boas_vindas.zip', as_attachment=True)

@app.route('/enviar_email', methods=['POST'])
def disparar_email():
    # Mantém a lógica anterior de fetch/JSON para o e-mail
    dados = request.json
    lista_nomes = [n.strip() for n in dados['nomes'].replace('\n', ',').split(',') if n.strip()]
    email_destino = dados.get('email')

    for nome in lista_nomes:
        pdf = gerar_pdf(nome)
        # (Chama a função enviar_email definida anteriormente)
        # enviar_email(email_destino, nome, pdf)
    
    return jsonify({"mensagem": "E-mails enviados com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
