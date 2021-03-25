def get_sma_20_data(data):
    sma_20_data = data.Close.rolling(window=20).mean()
    return sma_20_data
