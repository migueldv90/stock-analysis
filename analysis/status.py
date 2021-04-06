def get_status(macd_one, macd_two):
    status = ''

    if macd_one > 0 and macd_two < 0:
        status = 'Buy - watchlist'
    elif macd_one < 0 and macd_two > 0:
        status = 'Sell - watchlist'

    elif macd_one > 0:
        status = 'Buy - Hold'
    elif macd_one < 0:
        status = 'Sell - Hold'

    return status
