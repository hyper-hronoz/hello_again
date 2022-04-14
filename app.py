from email.policy import default
from multiprocessing import context
from flask import Flask, render_template

app = Flask(__name__)

planet_info = {
    "venus": ["Не живая", "Горячо", "Кислотные дожди", "Godness of decay"],
    "nothing": ["Enter planet name"]
}

@app.route("/choice", defaults={"planet" : "nothing"})
@app.route("/choice/", defaults={"planet" : "nothing"})
@app.route("/choice/<planet>")
def choice(planet):
    context = {}
    if planet in planet_info:
        context["facts"] = planet_info[planet]

    context["planet_name"] = planet
    return render_template("index.html", context=context)