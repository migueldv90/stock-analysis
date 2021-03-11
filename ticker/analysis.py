import numpy
import yfinance


def ticker_analysis(ticker, time_period, time_interval, file):
    data = yfinance.download(ticker, period=time_period, interval=time_interval, prepost=True)

    low_10 = data.Low.rolling(10).min()
    high_10 = data.High.rolling(10).max()

    sma_10 = data.Close.rolling(window=10).mean()
    sma_20 = data.Close.rolling(window=20).mean()

    ema_10 = data.Close.ewm(span=10, adjust=False).mean()
    ema_20 = data.Close.ewm(span=20, adjust=False).mean()

    macd = ema_10 - ema_20

    macd_angle_one = numpy.rad2deg(numpy.arctan2(macd[macd.size - 1] - macd[macd.size - 2], 1))
    macd_angle_two = numpy.rad2deg(numpy.arctan2(macd[macd.size - 2] - macd[macd.size - 3], 1))

    stoch_one = ((data.Close[data.Close.size - 1] - low_10[low_10.size - 1]) / (high_10[high_10.size - 1] - low_10[low_10.size - 1])) * 100

    ticker_status = ''
    if stoch_one > 80:
        ticker_status = 'Buy - Hold'
    elif stoch_one < 20:
        ticker_status = 'Sell - Hold'
    elif macd_angle_one > 0 and stoch_one > 20:
        ticker_status = 'Buy'
    elif macd_angle_one < 0 and stoch_one < 80:
        ticker_status = 'Sell'
    elif macd_angle_one > 0 and macd_angle_two < 0:
        ticker_status = 'Buy - Now'
    elif macd_angle_one < 0 and macd_angle_two > 0:
        ticker_status = 'Sell - Now'

    print('Ticker:', file=file)
    print(ticker + ' - ' + time_interval + ' - ' + ticker_status, file=file)

    print('Price:', file=file)
    print(data.Close[data.Close.size - 1], file=file)

    print('Ema 10:', file=file)
    print(ema_10[ema_10.size - 1], file=file)

    print('Sma 10:', file=file)
    print(sma_10[sma_10.size - 1], file=file)

    print('Sma 20:', file=file)
    print(sma_20[sma_20.size - 1], file=file)

    print('Macd:', file=file)
    print(macd[macd.size - 1], file=file)

    print('Macd Angle:', file=file)
    print(macd_angle_one, file=file)

    print('Stoch', file=file)
    print(stoch_one, file=file)

    print('', file=file)
