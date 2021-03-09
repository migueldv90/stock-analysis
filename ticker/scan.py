import numpy
import yfinance


def ticker_scan(ticker, time_period, time_interval, file):
    data = yfinance.download(ticker, period=time_period, interval=time_interval, prepost=True)

    sma_10 = data.Close.rolling(window=10).mean()
    sma_20 = data.Close.rolling(window=20).mean()

    ema_10 = data.Close.ewm(span=10, adjust=False).mean()
    ema_20 = data.Close.ewm(span=20, adjust=False).mean()

    ema_10_delta = ema_10[ema_10.size - 1] - ema_10[ema_10.size - 2]
    ema_10_delta_percent = (ema_10_delta / ema_10[ema_10.size - 1]) * 100

    macd = ema_10 - ema_20

    macd_angle = numpy.rad2deg(numpy.arctan2(macd[macd.size - 1] - macd[macd.size - 2], 1))
    macd_acceleration = (macd[macd.size - 1] - macd[macd.size - 2]) - (macd[macd.size - 2] - macd[macd.size - 3])

    low_10 = data.Low.rolling(10).min()
    high_10 = data.High.rolling(10).max()
    stoch = ((data.Close[data.Close.size - 1] - low_10[low_10.size - 1]) / (high_10[high_10.size - 1] - low_10[low_10.size - 1])) * 100

    ticker_status = ''
    if macd_angle > 0 and macd_acceleration > 0 and stoch > 20:
        ticker_status = 'Buy'
    elif macd_angle < 0 and macd_acceleration < 0 and stoch < 80:
        ticker_status = 'Sell'
    elif stoch > 80:
        ticker_status = 'Hold Buy'
    elif stoch < 20:
        ticker_status = 'Hold Sell'
    else:
        ticker_status = 'Hold'

    if ticker_status == 'Buy' or ticker_status == 'Hold Buy':
        print('Ticker:', file=file)
        print(ticker + ' - ' + time_interval + ' - ' + ticker_status, file=file)

        print('Price:', file=file)
        print(data.Close[data.Close.size - 1], file=file)

        print('Sma 10:', file=file)
        print(sma_10[sma_10.size - 1], file=file)

        print('Sma 20:', file=file)
        print(sma_20[sma_20.size - 1], file=file)

        print('Ema 10:', file=file)
        print(ema_10[ema_10.size - 1], file=file)

        print('Ema 10 Delta:', file=file)
        print(ema_10_delta, file=file)

        print('Ema 10 Delta Percent:', file=file)
        print(ema_10_delta_percent, file=file)

        print('Macd:', file=file)
        print(macd[macd.size - 1], file=file)

        print('Macd Angle:', file=file)
        print(macd_angle, file=file)

        print('Macd Acceleration', file=file)
        print(macd_acceleration, file=file)

        print('Stoch', file=file)
        print(stoch, file=file)

        print('', file=file)
