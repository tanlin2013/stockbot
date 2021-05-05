import unittest
from datetime import datetime
from stockbot.ticker.core import Ticker
from stockbot.constant import MovingAveragePeriod as MAv
from stockbot.constant import BackendAPI


class TestStockBot(unittest.TestCase):

    def test_history(self):
        ticker = Ticker('2330.TW', BackendAPI.Yahoo)
        df = ticker.history(period=MAv.SixMth)
        print(df)

    def test_kbars(self):
        ticker = Ticker('2330', BackendAPI.SinoTrade)
        df = ticker.kbars(
            datetime(2021, 4, 1),
            datetime(2021, 4, 23)
        )
        print(df)

    def test_technical_indicator(self):
        ticker = Ticker('2330.TW', BackendAPI.Yahoo)
        df = ticker.history(period=MAv.SixMth)
        ti = ticker.technical_indicator(
            'SMA',
            df,
            price='Close',
            timeperiod=5
        )
        print(ti.head(10))


if __name__ == '__main__':
    unittest.main()
