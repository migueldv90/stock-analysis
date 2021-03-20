def get_stoch_index(data, index):
    low_10 = data.Low.rolling(10).min()
    high_10 = data.High.rolling(10).max()
    return((data.Close[data.Close.size - index] - low_10[low_10.size - index]) / (high_10[high_10.size - index] - low_10[low_10.size - index])) * 100


def get_stoch_diff(stoch_one, stoch_two):
    return stoch_one - stoch_two
