import numpy
import yfinance


def ticker_analysis(ticker, time_frame, file):
    data = yfinance.download(ticker, period="5d", interval=time_frame, prepost=True)

    sma_10 = data.Close.rolling(window=10).mean()
    sma_20 = data.Close.rolling(window=20).mean()

    ema_10 = data.Close.ewm(span=10, adjust=False).mean()
    ema_20 = data.Close.ewm(span=20, adjust=False).mean()

    ema_10_delta = ema_10[ema_10.size - 2] - ema_10[ema_10.size - 3]
    ema_10_delta_percent = (ema_10_delta / ema_10[ema_10.size - 2]) * 100

    macd = ema_10 - ema_20

    macd_angle = numpy.rad2deg(numpy.arctan2(macd[macd.size - 2] - macd[macd.size - 3], 1))
    macd_acceleration = (macd[macd.size - 2] - macd[macd.size - 3]) - (macd[macd.size - 3] - macd[macd.size - 4])

    low_10 = data.Low.rolling(10).min()
    high_10 = data.High.rolling(10).max()
    stoch = ((data.Close[data.Close.size - 2] - low_10[low_10.size - 2]) / (high_10[high_10.size - 2] - low_10[low_10.size - 2])) * 100

    ticker_status = ''
    if macd_angle > 0 and macd_acceleration > 0 and stoch > 20:
        ticker_status = 'Buy'
    elif macd_angle < 0 and macd_acceleration < 0 and stoch < 80:
        ticker_status = 'Sell'
    else:
        ticker_status = 'Hold'

    print('Ticker: ' + ticker_status, file=file)
    print(ticker + ' - ' + time_frame, file=file)

    print('Ema 10 Delta:', file=file)
    print(ema_10_delta, file=file)

    print('Ema 10 Delta Percent:', file=file)
    print(ema_10_delta_percent, file=file)

    print('Macd Angle:', file=file)
    print(macd_angle, file=file)

    print('Macd Acceleration', file=file)
    print(macd_acceleration, file=file)

    print('Stoch', file=file)
    print(stoch, file=file)

    print('', file=file)
