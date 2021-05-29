from flask import Flask, render_template, logging, url_for

app = Flask(__name__, static_url_path='static', static_folder='static')


@app.route("/", methods=["GET"])
def index():
    app.logger.info("Moving to the index page")
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    app.logger.info("Moving to the about page")
    return render_template("about.html") 


@app.route("/gallery", methods=["GET"])
def gallery():
    app.logger.info("Moving to the gallery page")
    return render_template("gallery.html") 


@app.route("/kittytingz", methods=["GET"])
def kittytingz():
    app.logger.info("Moving to the kitty tingz page")
    return render_template("kittytingz.html") 


@app.route("/contact", methods=["GET"])
def contact():
    app.logger.info("Moving to the contact page")
    return render_template("contact.html") 


if __name__ == '__main__':
    port = int(5000)
    app.run(host='0.0.0.0', port=port, debug=True)
