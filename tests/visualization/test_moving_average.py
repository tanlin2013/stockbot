import unittest
from stockbot.ticker.yahoo import Market
from stockbot.visualization import MovingAverage
from stockbot.constant.yahoo import MovingAveragePeriod


class TestMovingAverage(unittest.TestCase):

    def test_plot(self):
        ticker = Market('2330.TW')
        df = ticker.history(period=MovingAveragePeriod.SixMth.value)
        MovingAverage.plot(
            df,
            title='2330',
            mav=(5, 10)
        )


if __name__ == '__main__':
    unittest.main()
