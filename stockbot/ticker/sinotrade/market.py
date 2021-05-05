import pandas as pd
from datetime import datetime
from typing import List
from shioaji.constant import *
from shioaji.order import Trade
from shioaji.contracts import Stock
from stockbot.ticker.sinotrade.session import Session
from stockbot.ticker.utils import *


class Market:

    def __init__(self, ticker_symbol: str, dry_run: bool = True, timeout: int = 10000) -> None:
        self.api = Session(timeout=timeout)
        self._ticker_symbol = ticker_symbol
        self._dry_run = dry_run
        # TODO: dry run is yet been implemented

    @property
    def ticker_symbol(self) -> str:
        return self._ticker_symbol

    @property
    def dry_run(self) -> bool:
        return self._dry_run

    def _stock(self, ticker_symbol: str) -> Stock:
        return self.api.Contracts.Stocks[ticker_symbol]

    @property
    def stock(self) -> Stock:
        return self._stock(self.ticker_symbol)

    @to_dataframe
    def ticks(self, date: datetime) -> pd.DataFrame:
        return self.api.ticks(self.stock, date.strftime('%Y-%m-%d'))

    @to_dataframe
    def kbars(self, start: datetime, end: datetime) -> pd.DataFrame:
        return self.api.kbars(
            self.stock,
            start=start.strftime('%Y-%m-%d'),
            end=end.strftime('%Y-%m-%d')
        )

    @to_dataframe
    def snapshot(self, ticker_symbols: List[str]) -> pd.DataFrame:
        return self.api.snapshots(list(map(self._stock, ticker_symbols)))

    def place_order(self,
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
            self.stock,
            order
        )

    def list_trades(self) -> List[Trade]:
        self.api.update_status(self.api.stock_account)
        return self.api.list_trades()

    def touch_price(self, topic, quote):
        # TODO:
        raise NotImplementedError

    def streaming(self,
                  quote_type: QuoteType = QuoteType.Tick,
                  intraday_odd: bool = False
                  ) -> None:
        self.api.quote.subscribe(
            contract=self.stock,
            quote_type=quote_type,
            intraday_odd=intraday_odd
        )
