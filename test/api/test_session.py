import unittest
from stockbot.api.session import Session


class TestSession(unittest.TestCase):

    def test_init(self):
        api = Session(dry_run=False)
        api.close()


if __name__ == '__main__':
    unittest.main()
