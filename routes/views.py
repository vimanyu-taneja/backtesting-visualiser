from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        ticker = request.form.get("ticker")
    return render_template("index.html", plot=ticker)
