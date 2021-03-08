import numpy
import yfinance


def ticker_analysis(ticker, file):
    data = yfinance.download(ticker, period="5d", interval="1h", prepost=True)

    short_sma = data.Close.rolling(window=10).mean()
    short_ema = data.Close.ewm(span=10, adjust=False).mean()
    long_ema = data.Close.ewm(span=20, adjust=False).mean()

    macd = short_ema - long_ema
    signal = macd.ewm(span=15, adjust=False).mean()

    macd_angle = numpy.rad2deg(numpy.arctan2(macd[macd.size - 1] - macd[macd.size - 2], 1))
    macd_velocity = macd[macd.size - 1] - macd[macd.size - 2]
    macd_acceleration = (macd[macd.size - 1] - macd[macd.size - 2]) - (macd[macd.size - 2] - macd[macd.size - 1])

    print('Ticker:', file=file)
    print(ticker, file=file)

    print('Price:', file=file)
    print(data.Close[data.Close.size - 1], file=file)

    print('Macd:', file=file)
    print(macd[macd.size - 1], file=file)

    print('Macd Angle:', file=file)
    print(macd_angle, file=file)

    print('Macd Velocity:', file=file)
    print(macd_velocity, file=file)

    print('Macd Acceleration', file=file)
    print(macd_acceleration, file=file)

    print('', file=file)
