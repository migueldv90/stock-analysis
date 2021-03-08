import numpy
import yfinance


def ticker_analysis(ticker, file):
    data = yfinance.download(ticker, period="5d", interval="30m", prepost=True)

    short_sma = data.Close.rolling(window=10).mean()
    long_sma = data.Close.rolling(window=20).mean()

    short_ema = data.Close.ewm(span=10, adjust=False).mean()
    long_ema = data.Close.ewm(span=20, adjust=False).mean()

    short_ema_percent = ((short_ema[short_ema.size - 1] - short_ema[short_ema.size - 2]) / short_ema[short_ema.size - 1]) * 100

    macd = short_ema - long_ema

    macd_angle = numpy.rad2deg(numpy.arctan2(macd[macd.size - 1] - macd[macd.size - 2], 1))
    macd_acceleration = (macd[macd.size - 1] - macd[macd.size - 2]) - (macd[macd.size - 2] - macd[macd.size - 1])

    print('Ticker:', file=file)
    print(ticker, file=file)

    print('Ema Percent:', file=file)
    print(short_ema_percent, file=file)

    print('Macd Angle:', file=file)
    print(macd_angle, file=file)

    print('Macd Acceleration', file=file)
    print(macd_acceleration, file=file)

    print('', file=file)
