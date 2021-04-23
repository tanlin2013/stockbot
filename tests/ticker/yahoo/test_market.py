import unittest
from stockbot.ticker.yahoo import Market
from stockbot.constant.yahoo import MovingAveragePeriod as MAv


class TestMarket(unittest.TestCase):

    ticker = Market('2330.TW')

    def test___str__(self):
        print(self.ticker)

    def test_ticker_code(self):
        self.assertEqual('2330.TW', self.ticker.ticker_symbol)

    def test_history(self):
        print(self.ticker.history(period=MAv.SixMth))


if __name__ == '__main__':
    unittest.main()
