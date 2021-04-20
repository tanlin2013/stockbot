import pandas as pd
from datetime import datetime
from typing import List, Callable
from shioaji.constant import *
from shioaji.order import Trade
from shioaji.contracts import Stock
from stockbot.ticker.sinotrade.session import Session


def to_dataframe(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> pd.DataFrame:
        _data = func(*args, **kwargs)
        df = pd.DataFrame(_data) if type(_data) is list \
            else pd.DataFrame({**_data})
        df.ts = pd.to_datetime(df.ts)
        return df
    return wrapper


class Market:

    def __init__(self, dry_run: bool = True, timeout: int = 10000) -> None:
        self.api = Session(timeout=timeout)
        self._dry_run = dry_run
        # TODO: dry run is yet been implemented

    @property
    def dry_run(self) -> bool:
        return self._dry_run

    def _stock(self, ticker_code: str) -> Stock:
        return self.api.Contracts.Stocks[ticker_code]

    @to_dataframe
    def ticks(self, ticker_code: str, date: datetime) -> pd.DataFrame:
        return self.api.ticks(self._stock(ticker_code), date.strftime('%Y-%m-%d'))

    @to_dataframe
    def kbars(self, ticker_code: str, start: datetime, end: datetime) -> pd.DataFrame:
        return self.api.kbars(
            self._stock(ticker_code),
            start=start.strftime('%Y-%m-%d'),
            end=end.strftime('%Y-%m-%d')
        )

    @to_dataframe
    def snapshot(self, ticker_codes: List[str]) -> pd.DataFrame:
        return self.api.snapshots(list(map(self._stock, ticker_codes)))

    def place_order(self,
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
            self._stock(ticker_code),
            order
        )

    def list_trades(self) -> List[Trade]:
        self.api.update_status(self.api.stock_account)
        return self.api.list_trades()

    def touch_price(self, topic, quote):
        # TODO:
        raise NotImplementedError

    def streaming(self,
                  ticker_code: str,
                  quote_type: QuoteType = QuoteType.Tick,
                  intraday_odd: bool = False
                  ) -> None:
        self.api.quote.subscribe(
            contract=self._stock(ticker_code),
            quote_type=quote_type,
            intraday_odd=intraday_odd
        )
