def get_status(macd_one, stoch_one, stoch_two, stoch_diff):
    status = ''

    if stoch_one >= 80 and stoch_two >= 80:
        status = 'Buy - Overbought'
    elif stoch_one <= 20 and stoch_two <= 20:
        status = 'Sell - Oversold'

    elif stoch_one >= 80 and stoch_two < 80:
        status = 'Buy - Upper'
    elif stoch_one <= 20 and stoch_two > 20:
        status = 'Sell - Lower'

    elif stoch_one >= 75 and stoch_diff > 0:
        status = 'Buy - Critical'
    elif stoch_one <= 25 and stoch_diff < 0:
        status = 'Sell - Critical'

    elif macd_one > 0:
        status = 'Buy - Hold'
    elif macd_one < 0:
        status = 'Sell - Hold'

    return status
