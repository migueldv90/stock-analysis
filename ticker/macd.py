def get_macd_data(data):
    ema_10 = data.Close.ewm(span=10, adjust=False).mean()
    ema_20 = data.Close.ewm(span=20, adjust=False).mean()
    macd_data = ema_10 - ema_20
    return macd_data


def get_macd_index(macd_data, index):
    return macd_data[macd_data.size - index]


def get_macd_diff(macd_one, macd_two):
    return macd_one - macd_two


def get_macd_direction(macd_diff):
    return'Positive'if macd_diff > 0 else'Negative'


def get_signal_data(macd_data):
    signal_data = macd_data.ewm(span=8, adjust=False).mean()
    return signal_data


def get_signal_index(signal_data, index):
    return signal_data[signal_data.size - index]


def get_signal_diff(signal_one, signal_two):
    return signal_one - signal_two
