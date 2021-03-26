def get_status(sma_20_diff, signal_diff):
    status = ''

    if signal_diff > 0 and sma_20_diff > 0:
        status = 'Buy - Strong'
    elif signal_diff < 0 and sma_20_diff < 0:
        status = 'Sell - Strong'

    elif sma_20_diff > 0:
        status = 'Buy - SMA'
    elif sma_20_diff < 0:
        status = 'Sell - SMA'

    elif signal_diff > 0:
        status = 'Buy - Signal'
    elif signal_diff < 0:
        status = 'Sell - Signal'

    return status
