from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/list")
def list():
    return render_template('list.html')

app.run(debug=True)