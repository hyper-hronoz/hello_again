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

@app.route("/carousel")
def index():
    return render_template("index.html")
