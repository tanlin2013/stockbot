from yfinance import Ticker
import mplfinance as mpf
import json
from typing import Tuple
from enum import Enum


class MovingAveragePeriod(Enum):
    OneDay = '1d'
    FiveDay = '5d'
    OneMth = '1mo'
    ThreeMth = '3mo'
    SixMth = '6mo'
    OneYear = '1y'
    TwoYear = '2y'
    FiveYear = '5y'
    TenYear = '10y'
    YearToDate = 'ytd'
    Max = 'max'


class YahooFinance(Ticker):

    def __init__(self, ticker_code: str):
        super(YahooFinance, self).__init__(ticker_code)
        self._ticker_code = ticker_code

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
