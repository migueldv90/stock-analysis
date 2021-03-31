def get_status(macd_one, macd_two, signal_diff, stoch_one, stoch_two, stoch_diff):
    status = ''

    if macd_one > 0 and macd_two < 0:
        status = 'Macd - Buy - Crossover'
    elif macd_one < 0 and macd_two > 0:
        status = 'Macd - Sell - Crossover'

    elif stoch_one >= 80 and signal_diff > 0 and macd_one < 0:
        status = 'Buy - Stoch - Overbought'
    elif stoch_one <= 20 and signal_diff < 0 and macd_one < 0:
        status = 'Sell - Stoch - Oversold'

    elif stoch_one >= 60 and stoch_diff > 0 and signal_diff > 0 and macd_one < 0:
        status = 'Buy - Stoch - Critical'
    elif stoch_one <= 40 and stoch_diff < 0 and signal_diff < 0 and macd_one < 0:
        status = 'Sell - Stoch - Critical'

    elif signal_diff > 0:
        status = 'Buy - Signal - Hold'
    elif signal_diff < 0:
        status = 'Sell - Signal - Hold'

    return status
