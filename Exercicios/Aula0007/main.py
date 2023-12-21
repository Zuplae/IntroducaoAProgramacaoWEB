from flask import Flask, render_template, request, redirect
from pacote import Pacote


app = Flask(__name__)

lista_pacotes = []

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    desc = request.form.get('desc')
    destino = request.form.get('destino')
    pacote = Pacote(nome, desc, destino)
    lista_pacotes.append(pacote)
    return redirect('/list')

@app.route('/list')
def list():
    return render_template('list.html', pacotes = lista_pacotes)

app.run(debug=True)