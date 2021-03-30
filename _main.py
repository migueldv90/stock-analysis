from ticker.analysis import analysis


from lists.etfs import tickers as etfs
from lists.crypto import tickers as crypto
from lists.stocks import tickers as stocks
from lists.webull import tickers as webull


def get_analysis(list, name, time_period, time_interval):
    file = open('_' + name + '-' + time_interval + '.txt', 'w')
    for ticker in list:
        analysis(ticker, time_period, time_interval, file)
    file.close()


time_period = '30d'
time_interval = '30m'

lists = [
    {
        'list': webull,
        'name': 'webull',
    },
]

for list in lists:
    get_analysis(list['list'], list['name'], time_period, time_interval)
