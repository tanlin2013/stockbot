from dataclasses import dataclass


@dataclass
class MovingAveragePeriod:
    OneDay: str = '1d'
    FiveDay: str = '5d'
    OneMth: str = '1mo'
    ThreeMth: str = '3mo'
    SixMth: str = '6mo'
    OneYear: str = '1y'
    TwoYear: str = '2y'
    FiveYear: str = '5y'
    TenYear: str = '10y'
    YearToDate: str = 'ytd'
    Max: str = 'max'
