def get_status(sma_20_diff_one, sma_20_diff_two, signal_diff_one, signal_diff_two):
    status = ''

    if signal_diff_one > 0 and sma_20_diff_one > 0 and sma_20_diff_two < 0:
        status = 'Buy - Strong - Now'
    elif signal_diff_one < 0 and sma_20_diff_one < 0 and sma_20_diff_two > 0:
        status = 'Sell - Strong - Now'

    elif signal_diff_one > 0 and sma_20_diff_one > 0:
        status = 'Buy - Strong'
    elif signal_diff_one < 0 and sma_20_diff_one < 0:
        status = 'Sell - Strong'

    elif signal_diff_one > 0 and signal_diff_two < 0:
        status = 'Buy - Watch'
    elif signal_diff_one < 0 and signal_diff_two > 0:
        status = 'Sell - Watch'

    elif signal_diff_one > 0:
        status = 'Buy'
    elif signal_diff_one < 0:
        status = 'Sell'

    return status
