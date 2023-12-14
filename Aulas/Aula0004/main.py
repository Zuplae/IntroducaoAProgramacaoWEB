from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    usuario = "Ana"
    return render_template('index.html', usuario=usuario)

@app.route("/create")
def create():
    return "Pagina de criação"

@app.route("/list")
def list():
    return "Página de listagem"

app.run(debug=True)