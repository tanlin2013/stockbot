import pandas as pd
from talib import abstract
from tsfresh.feature_extraction.feature_calculators import set_property
from stockbot.ticker.sinotrade import Market as SinoTrade
from stockbot.ticker.yahoo import Market as Yahoo
from stockbot.constant import BackendAPI


class Ticker:

    def __init__(self, ticker_symbol: str, backend: BackendAPI = BackendAPI.Yahoo, **kwargs) -> None:
        self.yahoo = Yahoo(ticker_symbol)
        self.sinotrade = SinoTrade(ticker_symbol, **kwargs)

    def technical_indicator(
            self,
            ti_name: str,
            inputs: pd.DataFrame,
            *args,
            **kwargs
    ) -> pd.DataFrame:
        return getattr(abstract, ti_name)(inputs, *args, **kwargs)
