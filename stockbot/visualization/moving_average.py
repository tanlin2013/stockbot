import mplfinance as mpf
import pandas as pd
from typing import Tuple


class MovingAverage:

    @staticmethod
    def plot(df: pd.DataFrame, title: str, mav: Tuple[int, int]):
        """

        Args:
            df
            title:
            mav:

        Returns:

        """
        style = mpf.make_mpf_style(
            base_mpf_style='yahoo',
            marketcolors=mpf.make_marketcolors(
                up='r',
                down='g',
                edge='',
                wick='inherit',
                volume='inherit'
            )
        )
        mpf.plot(
            df,
            type='candle',
            mav=mav,
            volume=True,
            style=style,
            title=title,
            ylabel_lower='Shares'
        )
