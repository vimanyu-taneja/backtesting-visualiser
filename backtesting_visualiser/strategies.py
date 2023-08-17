import pandas as pd
import ta
from backtesting import Strategy
from backtesting.lib import crossover


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
    strategies = {"RSI oscillator": RSIOscillator, "SMA crossover": SMACrossover}
    return strategies[name]
