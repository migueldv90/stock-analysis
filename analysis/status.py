def get_status(macd_one, macd_two, signal_diff, stoch_one, stoch_diff):
    status = ''

    if macd_one > 0 and macd_two < 0:
        status = 'Macd - Buy - Crossover'
    elif macd_one < 0 and macd_two > 0:
        status = 'Macd - Sell - Crossover'

    elif stoch_one >= 80 and signal_diff > 0 and macd_one > 0:
        status = 'Upper - Buy - Overbought'
    elif stoch_one <= 20 and signal_diff < 0 and macd_one > 0:
        status = 'Upper - Sell - Oversold'

    elif stoch_one >= 60 and stoch_diff > 0 and signal_diff > 0 and macd_one > 0:
        status = 'Upper - Buy - Critical'
    elif stoch_one <= 40 and stoch_diff < 0 and signal_diff < 0 and macd_one > 0:
        status = 'Upper - Sell - Critical'

    elif stoch_one >= 80 and signal_diff > 0 and macd_one < 0:
        status = 'Lower - Buy - Overbought'
    elif stoch_one <= 20 and signal_diff < 0 and macd_one < 0:
        status = 'Lower - Sell - Oversold'

    elif stoch_one >= 60 and stoch_diff > 0 and signal_diff > 0 and macd_one < 0:
        status = 'Lower - Buy - Critical'
    elif stoch_one <= 40 and stoch_diff < 0 and signal_diff < 0 and macd_one < 0:
        status = 'Lower - Sell - Critical'

    elif macd_one > 0:
        status = 'Macd - Buy - Hold'
    elif macd_one < 0:
        status = 'Macd - Sell - Hold'

    return status
