def get_status(macd_one, macd_two, signal_one, signal_two):
    status = ''

    if macd_one > 0 and macd_two < 0:
        status = 'Buy - Watchlist'
    elif macd_one < 0 and macd_two > 0:
        status = 'Sell - Watchlist'

    elif signal_one > 0:
        status = 'Buy - Hold'
    elif signal_two < 0:
        status = 'Sell - Hold'

    return status
