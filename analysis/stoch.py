def get_stoch_stoch_data(stoch_data):
    stoch_data['L10'] = stoch_data['Low'].rolling(window=10).min()
    stoch_data['H10'] = stoch_data['High'].rolling(window=10).max()
    stoch_data['%K'] = 100 * ((stoch_data['Close'] - stoch_data['L10']) / (stoch_data['H10'] - stoch_data['L10']))
    stoch_data['%D'] = stoch_data['%K'].rolling(window=3).mean()
    return stoch_data


def get_stoch_index(stoch_data, index):
    return stoch_data['%D'][stoch_data['%D'].size - index]


def get_stoch_diff(stoch_one, stoch_two):
    return stoch_one - stoch_two
