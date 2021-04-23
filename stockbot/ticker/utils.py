import pandas as pd
from typing import Callable


def to_dataframe(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> pd.DataFrame:
        _data = func(*args, **kwargs)
        df = pd.DataFrame(_data) if type(_data) is list \
            else pd.DataFrame({**_data})
        df.ts = pd.to_datetime(df.ts)
        return df
    return wrapper


def df_lower_columns(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> pd.DataFrame:
        df = func(*args, **kwargs)
        df.columns = df.columns.str.lower()
        return df
    return wrapper
