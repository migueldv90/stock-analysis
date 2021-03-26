import datetime
import threading
from ticker.analysis import analysis


from lists.webull import tickers as wb
from lists.crypto import tickers as cp
from lists.etfs import tickers as etfs
from lists.watchlist import tickers as wl


def stocks(time_period, time_interval):
    file = open('_stocks-' + time_interval + '.txt', 'w')
    for ticker in analysis_tickers:
        analysis(ticker, time_period, time_interval, file)
    file.close()


def scan(time_period, time_interval):
    file = open('_scan-' + time_interval + '.txt', 'w')
    for ticker in scan_tickers:
        analysis(ticker, time_period, time_interval, file)
    file.close()


def main(time_period, time_interval):
    stocks(time_period, time_interval)
    scan(time_period, time_interval)
    print(datetime.datetime.now().strftime('%m/%d/%y - %H:%M'))
    threading.Timer(1800, main).start()


time_period_30d = '30d'
time_interval_30m = '30m'


analysis_tickers = wb
scan_tickers = wl + cp + etfs


main(time_period_30d, time_interval_30m)
