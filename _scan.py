import datetime
import threading
from ticker.scan import ticker_scan


from tickers.watchlist import tickers as wl
from tickers.crypto import tickers as cp
from tickers.etfs import tickers as etfs


def main():
    file = open('_scan.txt', 'w')
    for ticker in tickers:
        ticker_scan(ticker, time_period, time_interval, file)
    file.close()

    print(datetime.datetime.now().strftime('%m/%d/%y - %H:%M'))
    threading.Timer(1800, main).start()


time_period = '30d'
time_interval = '1d'


tickers = wl + cp + etfs


main()
