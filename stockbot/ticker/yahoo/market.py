import json
from yfinance import Ticker
from stockbot.ticker.utils import *


class Market(Ticker):

    def __init__(self, ticker_symbol: str) -> None:
        self._ticker_symbol = ticker_symbol.upper()
        super(Market, self).__init__(self.ticker_symbol)

    @property
    def ticker_symbol(self) -> str:
        return self._ticker_symbol

    def __str__(self) -> str:
        return json.dumps(self.info, indent=4)

    @df_lower_columns
    def history(self, period="1mo", interval="1d",
                start=None, end=None, prepost=False, actions=True,
                auto_adjust=True, back_adjust=False,
                proxy=None, rounding=False, tz=None, **kwargs):
        return super(Market, self).history(
            period=period, interval=interval,
            start=start, end=end, prepost=prepost, actions=actions,
            auto_adjust=auto_adjust, back_adjust=back_adjust,
            proxy=proxy, rounding=rounding, tz=tz, **kwargs)
