import unittest
from stockbot.ticker.core import Ticker
from stockbot.constant import MovingAveragePeriod as MAv


class TestStockBot(unittest.TestCase):

    ticker = Ticker('5483.TWO')

    def test_history(self):
        df = self.ticker.history(period=MAv.SixMth)
        print(df)

    def test_technical_indicator(self):
        df = self.ticker.history(period=MAv.SixMth)
        ti = self.ticker.technical_indicator('SMA', df, time_period=5)
        print(ti)


if __name__ == '__main__':
    unittest.main()
