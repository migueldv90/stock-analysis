import datetime
import threading
from ticker.analysis import analysis


from lists.webull import tickers as wb
from lists.crypto import tickers as cp
from lists.etfs import tickers as etfs
from lists.watchlist import tickers as wl


def stocks():
    file = open('_stocks.txt', 'w')
    for ticker in analysis_tickers:
        analysis(ticker, time_period, time_interval, file)
    file.close()


def scan():
    file = open('_scan.txt', 'w')
    for ticker in scan_tickers:
        analysis(ticker, time_period, time_interval, file)
    file.close()


def main():
    stocks()
    scan()
    print(datetime.datetime.now().strftime('%m/%d/%y - %H:%M'))
    threading.Timer(1800, main).start()


time_period = '30d'
time_interval = '1d'


analysis_tickers = wb
scan_tickers = wl + cp + etfs


main()
