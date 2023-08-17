import pandas as pd
import ta
from backtesting import Strategy
from backtesting.lib import crossover


class BollingerBands(Strategy):
    init_size = 0.5
    order_times = []

    def init(self):
        close = self.data.Close
        self.signal = self.I(ta.volatility.bollinger_hband_indicator, pd.Series(close))

    def next(self):
        for j in range(0, len(self.orders)):
            self.orders[0].cancel()
            self.order_times.pop(0)

        if len(self.trades) > 0:
            if self.data.index[-1] >= 10:
                self.trades[-1].close()

            if self.trades[-1].is_long:
                self.trades[-1].close()
            elif self.trades[-1].is_short:
                self.trades[-1].close()

        if self.signal != 0 and len(self.trades) == 0:
            # Cancel previous orders
            for j in range(0, len(self.orders)):
                self.orders[0].cancel()
                self.order_times.pop(0)
            # Add new replacement order
            self.buy(sl=self.signal / 2, limit=self.signal, size=self.init_size)
            self.order_times.append(self.data.index[-1])

        elif self.signal != 0 and len(self.trades) == 0:
            # Cancel previous orders
            for j in range(0, len(self.orders)):
                self.orders[0].cancel()
                self.order_times.pop(0)
            # Add new replacement order
            self.sell(sl=self.signal * 2, limit=self.signal, size=self.init_size)
            self.order_times.append(self.data.index[-1])


class RSIOscillator(Strategy):
    upper_bound = 70
    lower_bound = 30

    def init(self):
        close = self.data.Close
        self.rsi = self.I(ta.momentum.rsi, pd.Series(close), 14)

    def next(self):
        if crossover(self.lower_bound, self.rsi):
            self.buy()
        elif crossover(self.rsi, self.upper_bound):
            self.sell()


class SMACrossover(Strategy):
    n1 = 50
    n2 = 100

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n1)
        self.sma2 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


def get_strategy(name):
    strategies = {
        "Bollinger bands": BollingerBands,
        "RSI oscillator": RSIOscillator,
        "SMA crossover": SMACrossover,
    }
    return strategies[name]
