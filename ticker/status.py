def get_status(macd_one, macd_diff, signal_one, signal_diff):
    status = ''

    if signal_diff > 0:
        status = 'Buy'
    elif signal_diff < 0:
        status = 'Sell'

    return status
