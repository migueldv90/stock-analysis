def get_status(stoch_one, stoch_two, stoch_diff_one):
    status = ''

    if stoch_one >= 80 and stoch_two >= 80:
        status = 'Buy - Overbought'
    elif stoch_one <= 20 and stoch_two <= 20:
        status = 'Sell - Oversold'

    elif stoch_one >= 80 and stoch_two < 80:
        status = 'Buy - Upper'
    elif stoch_one <= 20 and stoch_two > 20:
        status = 'Sell - Lower'

    elif stoch_one >= 75 and stoch_diff_one > 0:
        status = 'Buy - Critical'
    elif stoch_one <= 25 and stoch_diff_one < 0:
        status = 'Sell - Critical'

    elif stoch_diff_one > 0:
        status = 'Buy - Normal'
    elif stoch_diff_one < 0:
        status = 'Sell - Normal'

    return status
