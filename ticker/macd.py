def get_macd_data(data):
    ema_10 = data.Close.ewm(span=10, adjust=False).mean()
    ema_20 = data.Close.ewm(span=20, adjust=False).mean()
    macd_data = ema_10 - ema_20
    return macd_data


def get_macd_index(macd_data, index):
    return macd_data[macd_data.size - index]


def get_macd_diff(macd_one, macd_two):
    return macd_one - macd_two
