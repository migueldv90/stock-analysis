def get_status(macd_diff_one, macd_diff_two, stoch_one, stoch_diff_one):
    status = ''

    if stoch_one >= 80:
        status = 'Buy - Overbought'
    elif stoch_one <= 20:
        status = 'Sell - Oversold'

    # elif macd_diff_one > 0 and stoch_diff > 0 and ha_color_one == 'green' and ha_color_two == 'red':
    #     status = 'Buy - Now!'
    # elif macd_diff_one < 0 and stoch_diff < 0 and ha_color_one == 'red' and ha_color_two == 'green':
    #     status = 'Sell - Now!'

    # elif macd_diff_one > 0 and stoch_diff > 0 and ha_color_one == 'green':
    #     status = 'Buy - Now'
    # elif macd_diff_one < 0 and stoch_diff < 0 and ha_color_one == 'red':
    #     status = 'Sell - Now'

    elif macd_diff_one > 0:
        status = 'Buy'
    elif macd_diff_one < 0:
        status = 'Sell'

    return status
