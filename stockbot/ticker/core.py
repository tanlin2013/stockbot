import pandas as pd
from talib import abstract
from stockbot.ticker.sinotrade import Market as SinoTrade
from stockbot.ticker.yahoo import Market as Yahoo
from stockbot.constant import BackendAPI


class Ticker(Yahoo, SinoTrade):

    def __init__(self, ticker_symbol: str, dry_run: bool = True, timeout: int = 10000) -> None:
        super(Ticker, self).__init__(ticker_symbol)

    def technical_indicator(
            self,
            ti_name: str,
            inputs: pd.DataFrame,
            *args,
            **kwargs
    ) -> pd.DataFrame:
        return getattr(abstract, ti_name)(inputs, *args, **kwargs)
