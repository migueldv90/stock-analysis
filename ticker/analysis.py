import yfinance
from .status import get_status
from .stoch import get_stoch_index
from .macd import get_macd_data, get_macd_index, get_macd_diff, get_signal_data, get_signal_index, get_signal_diff


def analysis(ticker, time_period, time_interval, file):
    data = yfinance.download(ticker, period=time_period, interval=time_interval, prepost=True)

    macd_data = get_macd_data(data)
    macd_one = get_macd_index(macd_data, 1)
    macd_two = get_macd_index(macd_data, 2)
    macd_diff = get_macd_diff(macd_one, macd_two)

    signal_data = get_signal_data(macd_data)
    signal_one = get_signal_index(signal_data, 1)
    signal_two = get_signal_index(signal_data, 2)
    signal_diff = get_signal_diff(signal_one, signal_two)

    stoch = get_stoch_index(data, 1)

    status = get_status(macd_one, macd_diff, signal_one, signal_diff, stoch)

    print('Ticker:', file=file)
    print(ticker + ' - ' + time_interval + ' - ' + status, file=file)

    print('Price:', file=file)
    print(data.Close[data.Close.size - 1], file=file)

    print('Macd:', file=file)
    print(macd_one, file=file)

    print('Macd Diff:', file=file)
    print(macd_diff, file=file)

    print('Stoch:', file=file)
    print(stoch, file=file)

    print('', file=file)
