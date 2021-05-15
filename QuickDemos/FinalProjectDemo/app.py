from flask import Flask, render_template, logging

app = Flask(__name__)

@app.route("/")
def index():
    app.logger.info("Moving to the index page");
    return render_template("index.html") ;

@app.route("/dummy1")
def dummy1():
    app.logger.info("Moving to the dummy 1 page");
    return render_template("dummy1.html") 

@app.route("/dummy2")
def dummy2():
    app.logger.info("Moving to the dummy 2 page");
    return render_template("dummy2.html") 

@app.route("/dummy3")
def dummy3():
    app.logger.info("Moving to the dummy 3 page");
    return render_template("dummy3.html") 

@app.route("/dummy4")
def dummy4():
    app.logger.info("Moving to the dummy 4 page");
    return render_template("dummy4.html") 