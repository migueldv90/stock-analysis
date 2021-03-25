import yfinance
from .highlow import highlow
from .status import get_status
from .stoch import get_stoch_index, get_stoch_diff
from .macd import get_macd_data, get_macd_index, get_macd_diff


def analysis(ticker, time_period, time_interval, file):
    data = yfinance.download(ticker, period=time_period, interval=time_interval, prepost=True)
    l_min_max, l_min, l_max = highlow(data)

    macd_data = get_macd_data(data)
    macd_one = get_macd_index(macd_data, 1)
    macd_two = get_macd_index(macd_data, 2)
    macd_diff = get_macd_diff(macd_one, macd_two)

    stoch_one = get_stoch_index(data, 1)
    stoch_two = get_stoch_index(data, 2)
    stoch_diff = get_stoch_diff(stoch_one, stoch_two)

    status = get_status(macd_diff, stoch_one, stoch_diff)

    print('Ticker:', file=file)
    print(ticker + ' - ' + time_interval + ' - ' + status, file=file)

    print('Price:', file=file)
    print(data.Close[data.Close.size - 1], file=file)

    print('Macd:', file=file)
    print(macd_one, file=file)

    print('Macd Diff:', file=file)
    print(macd_diff, file=file)

    print('Stoch:', file=file)
    print(stoch_one, file=file)

    print('Stoch Diff:', file=file)
    print(stoch_diff, file=file)

    print('', file=file)
