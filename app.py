from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route("/list_prof", methods=["GET"], defaults={"list_type": ""})
@app.route("/list_prof/<list_type>", methods=["GET"])
def hello(list_type):
    context = {}

    context["error"] = ""

    if not list_type:
        context["error"] = "Да я тебя на марс отправлю! Вписал параметр быстро!"
    else:
        context["professions"] = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "не могли сразу готовый массив дать?"]

    context["list_type"] = list_type

    return render_template("index.html", context=context)