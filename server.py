from flask import Flask, render_template, request, url_for, redirect
from jinja2 import TemplateNotFound

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta' 

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/<path:subpath>')
def page(subpath):
    try:
        return render_template(f"{subpath}.html")
    except TemplateNotFound:
        return "Page not found", 404

@app.route('/thankyou')
def thankyou():
    email = request.args.get('email')
    return render_template('thankyou.html', email=email)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            email = data.get('email')
            return redirect(url_for('thankyou', email=email))
        except Exception as e:
            error = str(e)
            return f"An error occurred: {error}"
    else:
        return "Something went wrong. Try again!"
