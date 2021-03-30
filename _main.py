from ticker.analysis import analysis


from lists.etfs import tickers as etfs
from lists.crypto import tickers as crypto
from lists.stocks import tickers as stocks
from lists.webull import tickers as webull


def get_analysis(list, name, time_period, time_interval):
    file = open('output/' + name + '-' + time_interval + '.txt', 'w')
    for ticker in list:
        analysis(ticker, time_period, time_interval, file)
    file.close()


times = [
    {
        'time_period': '200d',
        'time_interval': '1d'
    },
]


lists = [
    {
        'list': etfs,
        'name': 'etfs',
    },
    {
        'list': crypto,
        'name': 'crypto',
    },
    {
        'list': stocks,
        'name': 'stocks',
    },
    {
        'list': webull,
        'name': 'webull',
    },
]


for time in times:
    for list in lists:
        get_analysis(list['list'], list['name'], time['time_period'], time['time_interval'])
