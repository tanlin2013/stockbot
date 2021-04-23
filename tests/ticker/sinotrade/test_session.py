import unittest
import shioaji as sj
from stockbot.ticker.sinotrade import Session


class TestSession(unittest.TestCase):

    session = Session()

    def test_session_account(self):
        self.assertTrue(
            isinstance(
                self.session.stock_account,
                sj.account.StockAccount
            )
        )
        self.assertTrue(
            self.session.stock_account.person_id.startswith('PAPIUSER0')
        )


if __name__ == '__main__':
    unittest.main()
