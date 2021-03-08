import numpy
import yfinance


def ticker_analysis(ticker):
    data = yfinance.download(ticker, period="5d", interval="1h", prepost=True)

    short_sma = data.Close.rolling(window=10).mean()
    short_ema = data.Close.ewm(span=10, adjust=False).mean()
    long_ema = data.Close.ewm(span=20, adjust=False).mean()

    macd = short_ema - long_ema
    signal = macd.ewm(span=15, adjust=False).mean()

    macd_angle = numpy.rad2deg(numpy.arctan2(macd[macd.size - 1] - macd[macd.size - 2], 1))
    velocity = macd[macd.size - 1] - macd[macd.size - 2]

    print('Ticker:')
    print(ticker)

    print('Price:')
    print(data.Close[data.Close.size - 1])

    print('Macd:')
    print(macd[macd.size - 1])

    print('Macd Angle:')
    print(macd_angle)

    print('Velocity:')
    print(velocity)

    print('')
