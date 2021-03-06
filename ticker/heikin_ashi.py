import pandas as pd


def get_heikin_ashi_data(data):
    heikin_ashi_data = pd.DataFrame(index=data.index.values, columns=['Open', 'High', 'Low', 'Close'])
    heikin_ashi_data['Close'] = (data['Open'] + data['High'] + data['Low'] + data['Close']) / 4

    for i in range(len(data)):
        if i == 0:
            heikin_ashi_data.iat[0, 0] = data['Open'].iloc[0]
        else:
            heikin_ashi_data.iat[i, 0] = (heikin_ashi_data.iat[i - 1, 0] + heikin_ashi_data.iat[i - 1, 3]) / 2

    heikin_ashi_data['High'] = heikin_ashi_data.loc[:, ['Open', 'Close']].join(data['High']).max(axis=1)
    heikin_ashi_data['Low'] = heikin_ashi_data.loc[:, ['Open', 'Close']].join(data['Low']).min(axis=1)

    return heikin_ashi_data


def get_heikin_ashi_color(heikin_ashi_data, index):
    open = heikin_ashi_data.Open[heikin_ashi_data.Open.size - index]
    close = heikin_ashi_data.Close[heikin_ashi_data.Close.size - index]
    color = 'green'if(open < close)else'red'if(open > close)else'white'
    return color
