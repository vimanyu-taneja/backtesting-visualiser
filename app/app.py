import os

from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/generate_plot", methods=["POST"])
def generate_plot():
    data = request.form
    ticker = data.get("ticker")
    return f"<p>{ticker}</p>"


if __name__ == "__main__" and os.getenv("FLASK_ENV"):
    app.run(host="127.0.0.1", port=8000, debug=True)