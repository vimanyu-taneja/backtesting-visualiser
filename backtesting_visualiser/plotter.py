from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import GOOG, SMA
from bs4 import BeautifulSoup


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


def stringify_html_file(file_path):
    try:
        with open(file_path, "r") as html_file:
            html_content = html_file.read()
            return html_content
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return None


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
        GOOG,
        SmaCross,
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


def test():
    return """<div class="notification is-link">
  <button class="delete"></button>
  Primar lorem ipsum dolor sit amet, consectetur
  adipiscing elit lorem ipsum dolor. <strong>Pellentesque risus mi</strong>, tempus quis placerat ut, porta nec nulla. Vestibulum rhoncus ac ex sit amet fringilla. Nullam gravida purus diam, et dictum <a>felis venenatis</a> efficitur.
</div>"""
