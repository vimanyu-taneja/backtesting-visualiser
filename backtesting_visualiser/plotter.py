import yfinance as yf
from backtesting import Backtest
from bs4 import BeautifulSoup

from backtesting_visualiser.strategies import get_strategy


def stringify_html_file(file_path):
    with open(file_path, "r") as html_file:
        html_content = html_file.read()
        return html_content


def extract_body_from_html(html_string):
    soup = BeautifulSoup(html_string, "html.parser")
    body = soup.body
    if body:
        return str(body)
    else:
        return None


def generate_plot(
    file_path,
    ticker,
    strategy_name,
    initial_cash=10_000,
    commission=0.0,
    margin=1.0,
    trade_on_close=False,
    hedging=False,
    exclusive_orders=False,
):
    bt = Backtest(
        yf.download(ticker, start="2018-01-01"),
        get_strategy(strategy_name),
        cash=initial_cash,
        commission=commission,
        margin=margin,
        trade_on_close=trade_on_close,
        hedging=hedging,
        exclusive_orders=exclusive_orders,
    )
    stats = bt.run()
    print(stats)
    bt.plot(filename=file_path, open_browser=False)
    return extract_body_from_html(stringify_html_file(file_path))
