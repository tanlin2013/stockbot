import unittest
from stockbot.ticker.api.sinotrade.market import Market


class TestMarket(unittest.TestCase):

    market = Market(dry_run=True)

    def test_trade(self):
        trade = self.market.trade(
            ticker_code='2330',
            price=600,
            quantity=10
        )
        print(type(trade))

    def test_update_status(self):
        trade = self.market.trade(
            ticker_code='2330',
            price=600,
            quantity=10
        )
        status = self.market.update_status()
        print(status)


if __name__ == '__main__':
    unittest.main()
