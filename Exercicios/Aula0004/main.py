from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Seja bem-vindo ao AirBNB"

@app.route("/create")
def create():
    return "Criação de pacotes de viagem"

@app.route("/list")
def list():
    return "Rota de listagem de pacotes de viagem"

app.run(debug=True)