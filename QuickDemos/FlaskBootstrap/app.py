from flask import Flask, render_template
from random import randint
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def name(name=None):
    names=["Fred", "Jack", "Ashley", "Angellica"]
    name=names[randint(0,3)]
    return render_template("index.html", name=name)

@app.route('/age')
def age():
    return 'Hey!' 


