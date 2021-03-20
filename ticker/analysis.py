import numpy
import yfinance
from .heikin_ashi import get_heikin_ashi_data, get_heikin_ashi_color


def ticker_analysis(ticker, time_period, time_interval, file):
    data = yfinance.download(ticker, period=time_period, interval=time_interval, prepost=True)

    heikin_ashi_data = get_heikin_ashi_data(data)
    ha_color_one = get_heikin_ashi_color(heikin_ashi_data, 1)
    ha_color_two = get_heikin_ashi_color(heikin_ashi_data, 2)

    ema_10 = data.Close.ewm(span=10, adjust=False).mean()
    ema_20 = data.Close.ewm(span=20, adjust=False).mean()

    macd = ema_10 - ema_20

    macd_one = macd[macd.size - 1]
    macd_two = macd[macd.size - 2]

    macd_angle = numpy.rad2deg(numpy.arctan2(macd_one - macd_two, 1))

    low_10 = data.Low.rolling(10).min()
    high_10 = data.High.rolling(10).max()

    stoch_one = ((data.Close[data.Close.size - 1] - low_10[low_10.size - 1]) / (high_10[high_10.size - 1] - low_10[low_10.size - 1])) * 100
    stoch_two = ((data.Close[data.Close.size - 2] - low_10[low_10.size - 2]) / (high_10[high_10.size - 2] - low_10[low_10.size - 2])) * 100

    stoch_angle = numpy.rad2deg(numpy.arctan2(stoch_one - stoch_two, 1))

    ticker_status = ''
    if stoch_one > 80:
        ticker_status = 'Buy - Hold'
    elif stoch_one < 20:
        ticker_status = 'Sell - Hold'
    elif macd_angle > 0 and stoch_angle > 0 and ha_color_one == 'green' and ha_color_two == 'red':
        ticker_status = 'Buy - Now!'
    elif macd_angle < 0 and stoch_angle < 0 and ha_color_one == 'red' and ha_color_two == 'green':
        ticker_status = 'Sell - Now!'
    elif macd_angle > 0 and stoch_angle > 0 and ha_color_one == 'green':
        ticker_status = 'Buy - Now'
    elif macd_angle < 0 and stoch_angle < 0 and ha_color_one == 'red':
        ticker_status = 'Sell - Now'
    elif macd_angle > 0:
        ticker_status = 'Buy - Hold'
    elif macd_angle < 0:
        ticker_status = 'Sell - Hold'

    print('Ticker:', file=file)
    print(ticker + ' - ' + time_interval + ' - ' + ticker_status, file=file)

    print('Price:', file=file)
    print(data.Close[data.Close.size - 1], file=file)

    print('Heikin Ashi:', file=file)
    print(ha_color_one, file=file)

    print('Macd:', file=file)
    print(macd_one, file=file)

    print('Macd Angle:', file=file)
    print(macd_angle, file=file)

    print('Stoch', file=file)
    print(stoch_one, file=file)

    print('Stoch Angle', file=file)
    print(stoch_angle, file=file)

    print('', file=file)
