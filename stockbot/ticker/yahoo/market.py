import json
from yfinance import Ticker


class Market(Ticker):

    def __init__(self, ticker_code: str) -> None:
        super(Market, self).__init__(ticker_code)
        self._ticker_code = ticker_code.upper()

    @property
    def ticker_code(self) -> str:
        return self._ticker_code

    def __str__(self) -> str:
        return json.dumps(self.info, indent=4)
