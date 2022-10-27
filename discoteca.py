from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='canciones')

app.run(host="0.0.0.0", port=5000)