def get_status(stoch_one, stoch_two, stoch_three, stoch_diff_one, stoch_diff_two):
    status = ''

    if stoch_one > 80:
        status = 'Buy - Hold'
    elif stoch_one < 20:
        status = 'Sell - Sell'

    elif stoch_one >= 75 and stoch_diff_one > 0:
        status = 'Buy - Critical'
    elif stoch_one <= 25 and stoch_diff_one < 0:
        status = 'Sell - Critical'

    elif stoch_diff_one > 0 and stoch_diff_two < 0:
        status = 'Buy - Direction'
    elif stoch_diff_one < 0 and stoch_diff_two > 0:
        status = 'Sell - Direction'

    elif stoch_diff_one > 0:
        status = 'Buy'
    elif stoch_diff_one < 0:
        status = 'Sell'

    return status
