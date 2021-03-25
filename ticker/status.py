def get_status(sma_20_diff, signal_diff):
    status = ''

    if signal_diff > 0 and sma_20_diff > 0:
        status = 'Buy - Strong'
    elif signal_diff < 0 and sma_20_diff < 0:
        status = 'Sell - Strong'

    elif signal_diff > 0:
        status = 'Buy'
    elif signal_diff < 0:
        status = 'Sell'

    return status
