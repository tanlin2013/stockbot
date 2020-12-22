import pandas as pd
from datetime import datetime
from stockbot.api.session import Session


class History:

    @classmethod
    def from_ticker(cls: Session, ticker_code: str, date) -> pd.DataFrame:
        ticks = cls.api.ticks(
            cls.api.Contracts.Stocks[ticker_code]
        )
        df = pd.DataFrame({**ticks})
        df.ts = pd.to_datetime(df.ts)
        return df
