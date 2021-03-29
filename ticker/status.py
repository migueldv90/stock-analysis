def get_status(macd_one, macd_two, stoch_one, stoch_two, stoch_diff):
    status = ''

    if stoch_one >= 80 and stoch_two >= 80 and macd_one < 0:
        status = 'Buy - Stoch - Overbought'
    elif stoch_one <= 20 and stoch_two <= 20 and macd_one < 0:
        status = 'Sell - Stoch - Oversold'

    elif stoch_one >= 80 and stoch_two < 80 and macd_one < 0:
        status = 'Buy - Stoch - Upper'
    elif stoch_one <= 20 and stoch_two > 20 and macd_one < 0:
        status = 'Sell - Stoch - Lower'

    elif stoch_one >= 75 and stoch_diff > 0 and macd_one < 0:
        status = 'Buy - Stoch - Critical'
    elif stoch_one <= 25 and stoch_diff < 0 and macd_one < 0:
        status = 'Sell - Stoch - Critical'

    elif macd_one > 0 and macd_two < 0:
        status = 'Buy - Macd - crossover'
    elif macd_one < 0 and macd_two > 0:
        status = 'Sell - Macd - crossover'

    elif macd_one > 0:
        status = 'Buy - Macd - Hold'
    elif macd_one < 0:
        status = 'Sell - Macd - Hold'

    return status
