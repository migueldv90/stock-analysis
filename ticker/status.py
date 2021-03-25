def get_status(l_min_max, l_min, l_max, macd_diff, stoch_one, stoch_diff):
    status = ''

    if stoch_one >= 80:
        status = 'Buy - Overbought'
    elif stoch_one <= 20:
        status = 'Sell - Oversold'

    elif macd_diff > 0:
        status = 'Buy'
    elif macd_diff < 0:
        status = 'Sell'

    return status
