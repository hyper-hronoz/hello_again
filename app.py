import imp
import os
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "templates"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['UPLOAD_FOLDER'] = "static"
app.secret_key = "ЕХАЛГРЕКА"
db = SQLAlchemy(app)

@app.route("/load_photo")
def index():
    return render_template("index.html", link=session.get("path", ""))

@app.route('/upload', methods = ["POST"])
def upload_file():
    file = request.files['file']
    file_name = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(file_path)
    session["path"] = "/static/" + file_name
    return render_template("index.html", link=session.get("path", ""))