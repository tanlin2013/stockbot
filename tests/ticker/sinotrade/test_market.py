import unittest
from datetime import datetime
from stockbot.ticker.sinotrade.market import Market


class TestMarket(unittest.TestCase):

    market = Market('2330')

    def test_ticks(self):
        df = self.market.ticks(
            datetime(2020, 6, 1)
        )
        print("ticks:")
        print(df)

    def test_kbars(self):
        df = self.market.kbars(
            datetime(2020, 6, 1),
            datetime(2020, 7, 1)
        )
        print("kbars:")
        print(df)

    def test_update_status(self):
        status = self.market.list_trades()
        print("status:")
        print(status)

    def test_snapshot(self):
        snapshot = self.market.snapshot(['2330', '2454'])
        print("snapshot:")
        print(snapshot)


if __name__ == '__main__':
    unittest.main()
