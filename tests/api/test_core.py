import unittest
from stockbot.ticker.core import (
    Ticker,
    MovingAveragePeriod as MAv
)


class TestStockBot(unittest.TestCase):

    bot = Ticker("2330.TW", MAv.SixMth)

    def test_df(self):
        self.assertCountEqual(
            [
                'Open',
                'High',
                'Low',
                'Close',
                'Volume',
                'Dividends',
                'Stock Splits'
            ],
            self.bot.df
        )

    def test_strategy(self):
        self.assertEqual("All", self.bot.strategy.name)

    def test_strategy_setter(self):
        self.bot.strategy_setter(
            name="custom",
            indicators=[
                {'kind': "ema", "length": 8},
                {"kind": "ema", "length": 21},
                {"kind": "bbands", "length": 20, "col_names": ("BBL", "BBM", "BBU")},
                {"kind": "macd", "fast": 8, "slow": 21, "col_names": ("MACD", "MACD_H", "MACD_S")}
            ]
        )
        self.assertEqual("custom", self.bot.strategy.name)


if __name__ == '__main__':
    unittest.main()
