import numpy
import yfinance


def ticker_analysis(ticker, time_frame, file):
    data = yfinance.download(ticker, period="5d", interval=time_frame, prepost=True)

    sma_10 = data.Close.rolling(window=10).mean()
    sma_20 = data.Close.rolling(window=20).mean()

    ema_10 = data.Close.ewm(span=10, adjust=False).mean()
    ema_20 = data.Close.ewm(span=20, adjust=False).mean()

    ema_10_percent = ((ema_10[ema_10.size - 1] - ema_10[ema_10.size - 2]) / ema_10[ema_10.size - 1]) * 100

    macd = ema_10 - ema_20

    macd_angle = numpy.rad2deg(numpy.arctan2(macd[macd.size - 1] - macd[macd.size - 2], 1))
    macd_acceleration = (macd[macd.size - 1] - macd[macd.size - 2]) - (macd[macd.size - 2] - macd[macd.size - 1])

    print('Ticker:', file=file)
    print(ticker + ' - ' + time_frame, file=file)

    print('Ema 10 Percent:', file=file)
    print(ema_10_percent, file=file)

    print('Macd Angle:', file=file)
    print(macd_angle, file=file)

    print('MacdAcceleration', file=file)
    print(macd_acceleration, file=file)

    print('', file=file)
