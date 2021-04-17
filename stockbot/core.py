import pandas as pd
import pandas_ta as ta
from typing import List, Dict
from stockbot.constant.yahoo import MovingAveragePeriod
from stockbot.constant.strategy import BuiltinStrategy


class StockBot(Market):

    def __init__(self, ticker_code: str,
                 mav: MovingAveragePeriod = MovingAveragePeriod.SixMth,
                 builtin_strategy: BuiltinStrategy = BuiltinStrategy.All):
        super(StockBot, self).__init__(ticker_code)
        self._df = self.history(mav.value)
        self._strategy = ta.Strategy(builtin_strategy.value)

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @property
    def strategy(self) -> ta.Strategy:
        return self._strategy

    def strategy_setter(self, name: str, indicators: List[Dict]):
        self._strategy = ta.Strategy(
            name=name,
            ta=indicators
        )

    def exec(self):
        self._df.ta.strategy(self._strategy)
