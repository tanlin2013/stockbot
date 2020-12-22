from shioaji.constant import QuoteType
from stockbot.api.session import Session


class Streaming:

    @classmethod
    def from_ticker(cls: Session, ticker_code: str, intraday_odd: bool = False):
        return cls.api.quote.subscribe(
            contract=cls.api.Contracts.Stocks[ticker_code],
            quote_type=QuoteType.Tick,
            intraday_odd=intraday_odd
        )
