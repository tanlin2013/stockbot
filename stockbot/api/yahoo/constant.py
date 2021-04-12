from enum import Enum


class MovingAveragePeriod(Enum):
    OneDay = '1d'
    FiveDay = '5d'
    OneMth = '1mo'
    ThreeMth = '3mo'
    SixMth = '6mo'
    OneYear = '1y'
    TwoYear = '2y'
    FiveYear = '5y'
    TenYear = '10y'
    YearToDate = 'ytd'
    Max = 'max'
