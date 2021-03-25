def get_status(sma_20_diff_one, sma_20_diff_two, signal_diff):
    status = ''

    if signal_diff > 0 and sma_20_diff_one > 0 and sma_20_diff_two < 0:
        status = 'Buy - Now'
    elif signal_diff < 0 and sma_20_diff_one < 0 and sma_20_diff_two > 0:
        status = 'Sell - Now'

    elif signal_diff > 0 and sma_20_diff_one > 0:
        status = 'Buy - Strong'
    elif signal_diff < 0 and sma_20_diff_one < 0:
        status = 'Sell - Strong'

    elif signal_diff > 0:
        status = 'Buy'
    elif signal_diff < 0:
        status = 'Sell'

    return status
