import datetime
import threading
from analysis.analysis import analysis


from lists.etfs import tickers as etfs
from lists.crypto import tickers as crypto
from lists.stocks import tickers as stocks
from lists.webull import tickers as webull


times = [
    {
        'time_period': '200d',
        'time_interval': '1d',
    },
    {
        'time_period': '50d',
        'time_interval': '30m',
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


def main():
    for time in times:
        for list in lists:
            file = open('output/' + list['name'] + '-' + time['time_interval'] + '.txt', 'w')
            for ticker in list['list']:
                analysis(ticker, time['time_period'], time['time_interval'], file)
            file.close()
    print(datetime.datetime.now().strftime('%m/%d/%y - %H:%M'))
    threading.Timer(20, main).start()


main()
