from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY'] = "JFJWOFDSFAOIJF"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/resources")
def resources():
    df = pd.read_csv("api/static/data.csv").to_dict('records')
    return render_template('resources.html', resources=df)

@app.route("/quiz")
def quiz():
    return render_template('knowledge_quiz.html')

@app.route("/references")
def references():
    return render_template('references.html')

@app.route("/qr")
def qr():
    return render_template('qr.html')


if __name__ == '__main__':
    app.run(debug=True)
