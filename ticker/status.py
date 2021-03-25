def get_status(l_min_max, l_min, l_max, macd_diff, stoch):
    status = ''

    if stoch >= 80:
        status = 'Buy - Overbought'
    elif stoch <= 20:
        status = 'Sell - Oversold'

    elif macd_diff > 0:
        status = 'Buy'
    elif macd_diff < 0:
        status = 'Sell'

    return status
