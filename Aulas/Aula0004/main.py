from flask import Flask, render_template, request, redirect

app = Flask(__name__)
lista_produtos = []


@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/create")
def create():
    return render_template('create.html')

@app.route('/save', methods=["POST"])
def save():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    valor = request.form.get("valor")
    prod = {"nome":nome, "descricao": descricao, "valor": valor}
    lista_produtos.append(prod)
    return redirect('/list')


@app.route("/list")
def list():
    return render_template('list.html', lista = lista_produtos)

app.run(debug=True)

