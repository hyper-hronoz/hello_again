from email.policy import default
from multiprocessing import context
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/choice/<nickname>/<int:level>/<float:rating>")
def choice(nickname, level, rating):
    context = {}

    context["nickname"] = nickname
    context["facts"] = [f"Проздравляем! Ваш рейтинг после {level} этапа отбора", f"составляет {rating}", f"Желаем удачи!"]

    return render_template("index.html", context=context)