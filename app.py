from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route("/index/<title>", methods=["GET"])
def hello(title):
    image_source = "/static/1.jpg"

    if ("инженер" in title or "строитель" in title):
        image_source = "/static/2.png"

    return render_template("index.html", title=title, image_source=image_source)