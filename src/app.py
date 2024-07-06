from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.j2')

@app.route('/test')
def test_page():
    return render_template('firstpage.j2')