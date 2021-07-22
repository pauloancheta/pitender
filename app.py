from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/manual')
def manual():
    return render_template('manual.html')


@app.route('/recipes')
def recipes():
    return render_template('recipes.html')


@app.route('/bottle/<int:id>')
def bottle(id):
    return render_template('manual.html')
