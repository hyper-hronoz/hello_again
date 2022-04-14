from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route("/index/<title>", methods=["GET"])
def hello(title):
    return render_template("index.html", title=title)