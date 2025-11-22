"""Server file for Flask Portfolio Web Application."""

from flask import Flask, render_template, request, url_for, redirect
from jinja2 import TemplateNotFound

app = Flask(__name__)

# This import is for private deployment settings, not included in the repository
try:
    import deploy_private # pylint: disable=W0611 # type: ignore
except ImportError:
    pass

@app.route("/")
def home():
    """Home page."""
    return render_template("index.html")

@app.route('/<path:subpath>')
def page(subpath):
    """Page to render subpages."""
    try:
        return render_template(f"{subpath}.html")
    except TemplateNotFound:
        return "Page not found", 404

@app.route('/thankyou')
def thankyou():
    """Thank you page after form submission."""
    email = request.args.get('email')
    try:
        return render_template('thankyou.html', email=email)
    except TemplateNotFound:
        return "Page not found", 404

@app.route('/submit_form', methods=['POST'])
def submit_form():
    """Handles form submission."""
    if request.method == 'POST':
        data = request.form.to_dict()
        email = data.get('email')
        if not email:
            return "Missing required field: email", 400
        return redirect(url_for('thankyou', email=email))
    return "Something went wrong. Try again!", 400
