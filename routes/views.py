from flask import Blueprint, render_template

views = Blueprint("views", "views")


@views.route("/")
def home():
    return render_template("index.html")
