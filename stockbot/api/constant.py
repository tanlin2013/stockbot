from enum import Enum


class Action(Enum):
    buy = "Buy"
    sell = "Sell"


class OrderCond(Enum):
    cash = "Cash"
    netting = "Netting"
    margin_trading = "MarginTrading"
    short_selling = "ShortSelling"


class OrderLot(Enum):
    common = "Common"
    fixing = "Fixing"
    odd = "Odd"
