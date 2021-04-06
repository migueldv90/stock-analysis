def get_status(macd_one, macd_two, signal_one, signal_two):
    status = ''

    if signal_one > 0 and signal_two < 0:
        status = 'Buy - Now'
    elif signal_one < 0 and signal_two > 0:
        status = 'Sell - Now'

    elif macd_one > 0 and macd_two < 0:
        status = 'Buy - Watchlist'
    elif macd_one < 0 and macd_two > 0:
        status = 'Sell - Watchlist'

    elif signal_one > 0:
        status = 'Buy - Hold'
    elif signal_one < 0:
        status = 'Sell - Hold'

    return status
