def get_status(macd_one, macd_diff, signal_one, signal_diff, stoch):
    status = ''

    if stoch >= 80:
        status = 'Buy - Overbought'
    elif stoch <= 20:
        status = 'Sell - Oversold'

    elif signal_diff > 0:
        status = 'Buy'
    elif signal_diff < 0:
        status = 'Sell'

    return status
