import unittest
from stockbot.api.yahoo.market import Market
from stockbot.api.yahoo.constant import MovingAveragePeriod as MAv


class TestMarket(unittest.TestCase):

    ticker = Market('2330.TW')

    def test_ticker_code(self):
        self.assertEqual('2330.TW', self.ticker.ticker_code)

    def test_history(self):
        print(self.ticker.history(period=MAv.SixMth.value).tail(5))

    def test_plot(self):
        self.ticker.plot(
            period=MAv.SixMth,
            mav=(5, 10)
        )


if __name__ == '__main__':
    unittest.main()
