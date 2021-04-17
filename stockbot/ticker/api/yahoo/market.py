import json
import mplfinance as mpf
from yfinance import Ticker
from typing import Tuple
from stockbot.constant.yahoo import MovingAveragePeriod


class Market(Ticker):

    def __init__(self, ticker_code: str):
        super(Market, self).__init__(ticker_code)
        self._ticker_code = ticker_code.upper()

    @property
    def ticker_code(self) -> str:
        return self._ticker_code

    def __str__(self):
        return json.dumps(self.info, indent=4)

    def plot(self, period: MovingAveragePeriod, mav: Tuple[int, int]):
        """

        Args:
            period:
            mav:

        Returns:

        """
        style = mpf.make_mpf_style(
            base_mpf_style='yahoo',
            marketcolors=mpf.make_marketcolors(
                up='r',
                down='g',
                edge='',
                wick='inherit',
                volume='inherit'
            )
        )
        mpf.plot(
            self.history(period=period.value),
            type='candle',
            mav=mav,
            volume=True,
            style=style,
            title=self.ticker_code,
            ylabel_lower='Shares'
        )
