import yfinance
from .status import get_status
from .stoch import get_stoch_stoch_data, get_stoch_index, get_stoch_diff
from .sma import get_sma_20_data, get_sma_20_index, get_sma_20_diff
from .macd import get_macd_data, get_macd_index, get_macd_diff, get_macd_direction, get_signal_data, get_signal_index, get_signal_diff


def analysis(ticker, time_period, time_interval, file):
    data = yfinance.download(ticker, period=time_period, interval=time_interval, prepost=False)

    sma_20_data = get_sma_20_data(data)
    sma_20_one = get_sma_20_index(sma_20_data, 1)
    sma_20_two = get_sma_20_index(sma_20_data, 2)
    sma_20_diff = get_sma_20_diff(sma_20_one, sma_20_two)

    macd_data = get_macd_data(data)
    macd_one = get_macd_index(macd_data, 1)
    macd_two = get_macd_index(macd_data, 2)
    macd_diff = get_macd_diff(macd_one, macd_two)
    macd_direction = get_macd_direction(macd_diff)

    signal_data = get_signal_data(macd_data)
    signal_one = get_signal_index(signal_data, 1)
    signal_two = get_signal_index(signal_data, 2)
    signal_diff = get_signal_diff(signal_one, signal_two)

    stoch_stoch_data = get_stoch_stoch_data(data)
    stoch_one = get_stoch_index(stoch_stoch_data, 1)
    stoch_two = get_stoch_index(stoch_stoch_data, 2)
    stoch_three = get_stoch_index(stoch_stoch_data, 3)
    stoch_diff_one = get_stoch_diff(stoch_one, stoch_two)
    stoch_diff_two = get_stoch_diff(stoch_two, stoch_three)

    status = get_status(stoch_one, stoch_two, stoch_three, stoch_diff_one, stoch_diff_two)

    print('Ticker:', file=file)
    print(ticker + ' - ' + time_interval + ' - ' + status, file=file)

    print('Price:', file=file)
    print(data.Close[data.Close.size - 1], file=file)

    print('SMA 20:', file=file)
    print(sma_20_one, file=file)

    print('SMA 20 Diff:', file=file)
    print(sma_20_diff, file=file)

    print('Macd:' + macd_direction, file=file)
    print(macd_one, file=file)

    print('Macd Diff:', file=file)
    print(macd_diff, file=file)

    print('Signal:', file=file)
    print(signal_one, file=file)

    print('Signal Diff:', file=file)
    print(signal_diff, file=file)

    print('Stoch One:', file=file)
    print(stoch_one, file=file)

    print('Stoch Two:', file=file)
    print(stoch_two, file=file)

    print('Stoch Three:', file=file)
    print(stoch_three, file=file)

    print('Stoch Diff One:', file=file)
    print(stoch_diff_one, file=file)

    print('Stoch Diff Two:', file=file)
    print(stoch_diff_two, file=file)

    print('', file=file)
