from stockbot.ticker.api import Market


class MovingAverage(Market):

    def __init__(self, ticker_code: str):
        super(MovingAverage, self).__init__(ticker_code)

    def sma(self):
        return

    def ema(self):
        return


class MovingAverageConvergenceDivergence:

    def __init__(self):
        pass

    def macd(self):
        pass


class PairsTrading:

    def __init__(self):
        pass


class HeikinAshiCandlestick:

    def __init__(self):
        pass


class LondonBreakout:

    def __init__(self):
        pass


class AwesomeOscillator:

    def __init__(self):
        pass


class ParabolicStopAndReverse:

    def __init__(self):
        pass


class BollingerBands:

    def __init__(self):
        pass


class RelativeStrengthIndex:

    def __init__(self):
        pass
