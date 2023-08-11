import os

from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        ticker = data.get("ticker")
        return render_template("index.html", plot=ticker)
    return render_template("index.html")


if __name__ == "__main__" and os.getenv("FLASK_ENV"):
    app.run(host="127.0.0.1", port=5000, debug=True)
