def get_status(macd_one, macd_two, signal_diff, stoch_one, stoch_two, stoch_diff):
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
        status = 'Stoch - Buy - Overbought'
    elif stoch_one <= 20 and signal_diff < 0 and macd_one < 0:
        status = 'Stoch - Sell - Oversold'

    elif stoch_one >= 60 and stoch_diff > 0 and signal_diff > 0 and macd_one < 0:
        status = 'Stoch - Buy - Critical'
    elif stoch_one <= 40 and stoch_diff < 0 and signal_diff < 0 and macd_one < 0:
        status = 'Stoch - Sell - Critical'

    elif signal_diff > 0:
        status = 'Signal - Buy - Hold'
    elif signal_diff < 0:
        status = 'Signal - Sell - Hold'

    return status
