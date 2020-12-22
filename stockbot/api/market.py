import pandas as pd
from datetime import datetime
from shioaji.constant import QuoteType
from stockbot.api.session import Session
from stockbot.api.constant import *


class Stock:

    def __new__(cls, api, ticker_code: str):
        return api.Contracts.Stocks[ticker_code]


class Market(Session):

    def __init__(self, dry_run: bool = True, timeout: int = 10000):
        super(Market, self).__init__(dry_run, timeout)

    def streaming(self, ticker_code: str, intraday_odd: bool = False):
        self.api.quote.subscribe(
            contract=Stock(self.api, ticker_code),
            quote_type=QuoteType.Tick,
            intraday_odd=intraday_odd
        )

    def history(self, ticker_code: str, start: datetime, end: datetime):
        kbars = self.api.kbars(
            Stock(self.api, ticker_code),
            start=start,
            end=end
        )
        df = pd.DataFrame({**kbars})
        df.ts = pd.to_datetime(df.ts)
        return df

    def snapshot(self):
        return

    def trade(self, ticker_code: str, price: int, action: Action, quantity: int = 1):
        order = self.api.Order(
            price=price,
            quantity=quantity,
            action=action.value,
            price_type="LMT",
            order_type="ROD",
            order_lot="Common",
            account=self.api.stock_account
        )
        return self.api.place_order(
            Stock(self.api, ticker_code),
            order
        )
