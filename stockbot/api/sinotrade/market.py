import pandas as pd
from datetime import datetime
from typing import List
from shioaji.constant import *
from shioaji.order import Trade
from stockbot.api.sinotrade.session import Session


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

    def history(self, ticker_code: str, start: datetime, end: datetime) -> pd.DataFrame:
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

    def trade(self,
              ticker_code: str,
              price: float,
              quantity: int = 1,
              action: Action = Action.Buy,
              price_type: StockPriceType = StockPriceType.LMT,
              order_type: StockOrderType = StockOrderType.Common,
              order_lot: str = STOCK_ORDER_LOT_COMMON
              ) -> Trade:
        order = self.api.Order(
            price=price,
            quantity=quantity,
            action=action,
            price_type=price_type,
            order_type=order_type,
            order_lot=order_lot,
            account=self.api.stock_account
        )
        return self.api.place_order(
            Stock(self.api, ticker_code),
            order
        )

    def update_status(self) -> List[Trade]:
        self.api.update_status()
        return self.api.list_trades()

    def touch_price(self, topic, quote):
        raise NotImplementedError
