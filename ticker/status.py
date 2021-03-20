def get_status(macd_diff_one, macd_diff_two, stoch_one, stoch_diff_one):
    status = ''

    if stoch_one >= 80:
        status = 'Buy - Overbought'
    elif stoch_one <= 20:
        status = 'Sell - Oversold'

    elif macd_diff_one > 0 and macd_diff_two < 0:
        status = 'Buy - Now'
    elif macd_diff_one < 0 and macd_diff_two < 0:
        status = 'Sell - Now'

    elif macd_diff_one > 0 and stoch_diff_one > 0:
        status = 'Buy - Strong'
    elif macd_diff_one < 0 and stoch_diff_one < 0:
        status = 'Sell-Strong'

    elif macd_diff_one > 0:
        status = 'Buy'
    elif macd_diff_one < 0:
        status = 'Sell'

    return status
