import os

from dotenv import load_dotenv
from flask import Flask, render_template, request

from app.forms import ParamsForm
from backtesting_visualiser import plotter

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = "d3628918c1805d96607f47eaf3c659f60f28da61f393bf9a"


@app.route("/")
def home():
    return render_template("index.html", form=ParamsForm())


@app.route("/api/generate_plot", methods=["POST"])
def generate_plot():
    data = request.form
    file_path = "/tmp/plot.html" if os.getenv("VERCEL") else "plot.html"
    plot = plotter.generate_plot(
        file_path=file_path,
        ticker=data.get("ticker") or "GOOG",
        strategy_name=data.get("strategy"),
        initial_cash=int(data.get("initial_cash") or 1_000),
        commission=float(data.get("commission") or 2) / 100,
        margin=1 / float(data.get("leverage") or 1),
        trade_on_close=data.get("trade_on_close") == "Yes",
        hedging=data.get("allow_hedging") == "Yes",
        exclusive_orders=data.get("exclusive_orders") == "Yes",
    )
    return plot


if __name__ == "__main__" and os.getenv("FLASK_ENV"):
    app.run(host="127.0.0.1", port=8000, debug=True)
