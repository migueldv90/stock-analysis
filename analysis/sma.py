def get_sma_20_data(data):
    sma_20_data = data.Close.rolling(window=20).mean()
    return sma_20_data


def get_sma_20_index(sma_20_data, index):
    return sma_20_data[sma_20_data.size - index]


def get_sma_20_diff(sma_20_one, sma_20_two):
    return sma_20_one - sma_20_two
