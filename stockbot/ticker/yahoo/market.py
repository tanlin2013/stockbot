import json
from yfinance import Ticker


class Market(Ticker):

    def __init__(self, ticker_symbol: str) -> None:
        self._ticker_symbol = ticker_symbol.upper()
        super(Market, self).__init__(self.ticker_symbol)

    @property
    def ticker_symbol(self) -> str:
        return self._ticker_symbol

    def __str__(self) -> str:
        return json.dumps(self.info, indent=4)
