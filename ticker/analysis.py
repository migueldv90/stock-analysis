import yfinance
from .status import get_status
from .stoch import get_stoch_index, get_stoch_diff
from .macd import get_macd_data, get_macd_index, get_macd_diff
from .heikin_ashi import get_heikin_ashi_data, get_heikin_ashi_color


def ticker_analysis(ticker, time_period, time_interval, file):
    data = yfinance.download(ticker, period=time_period, interval=time_interval, prepost=True)

    heikin_ashi_data = get_heikin_ashi_data(data)
    ha_color_one = get_heikin_ashi_color(heikin_ashi_data, 1)
    ha_color_two = get_heikin_ashi_color(heikin_ashi_data, 2)

    macd_data = get_macd_data(data)
    macd_one = get_macd_index(macd_data, 1)
    macd_two = get_macd_index(macd_data, 2)
    macd_diff = get_macd_diff(macd_one, macd_two)

    stoch_one = get_stoch_index(data, 1)
    stoch_two = get_stoch_index(data, 2)
    stoch_diff = get_stoch_diff(stoch_one, stoch_two)

    status = get_status(ha_color_one, ha_color_two, macd_diff, stoch_one, stoch_diff)

    print('Ticker:', file=file)
    print(ticker + ' - ' + time_interval + ' - ' + status, file=file)

    print('Price:', file=file)
    print(data.Close[data.Close.size - 1], file=file)

    print('Heikin Ashi:', file=file)
    print(ha_color_one, file=file)

    print('Macd:', file=file)
    print(macd_one, file=file)

    print('Macd Diff:', file=file)
    print(macd_diff, file=file)

    print('Stoch', file=file)
    print(stoch_one, file=file)

    print('Stoch Diff', file=file)
    print(stoch_diff, file=file)

    print('', file=file)
