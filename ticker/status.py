def get_status(l_min_max, l_min, l_max, macd_diff, stoch):
    status = ''

    if stoch >= 80:
        status = 'Buy - Overbought'
    elif stoch <= 20:
        status = 'Sell - Oversold'

    elif l_min_max[-1] == l_min[-1] and macd_diff > 0:
        status = 'Buy - Now'
    elif l_min_max[-1] == l_max[-1] and macd_diff < 0:
        status = 'Sell - Now'

    elif macd_diff > 0:
        status = 'Buy'
    elif macd_diff < 0:
        status = 'Sell'

    return status
