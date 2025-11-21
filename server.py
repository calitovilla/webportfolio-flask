from flask import Flask, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/<path:subpath>')
def page(subpath):
    try:
        return render_template(f"{subpath}.html")
    except TemplateNotFound:
        return "Page not found", 404
