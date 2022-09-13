import os

from flask import Flask, render_template

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/preface")
def preface():
    return render_template("preface.html")

@app.route("/project_film")
def project_film():
    return render_template("project_film.html")

@app.route("/project_best")
def project_best():
    return render_template("project_best.html")

@app.route("/project_marketplace")
def project_marketplace():
    return render_template("project_marketplace.html")

@app.route("/project_movie")
def project_movie():
    return render_template("project_movie.html")

@app.route("/project_winetime")
def project_winetime():
    return render_template("project_winetime.html")

@app.route("/project_website")
def project_website():
    return render_template("project_website.html")

@app.route("/project_exqcorps")
def project_exqcorps():
    return render_template("project_exqcorps.html")
