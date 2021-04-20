import unittest
from datetime import datetime
from stockbot.ticker.sinotrade.market import Market


class TestMarket(unittest.TestCase):

    market = Market()

    def test_kbars(self):
        df = self.market.kbars(
            '2330',
            datetime(2020, 6, 1),
            datetime(2020, 7, 1)
        )
        print(df)

    def test_update_status(self):
        status = self.market.list_trades()
        print(status)

    def test_snapshot(self):
        snapshot = self.market.snapshot(['2330'])
        print(snapshot)


if __name__ == '__main__':
    unittest.main()
