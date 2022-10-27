from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>¡Hola Mundo de Programación Web!</h1>'

app.run(host="0.0.0.0", port=5000)