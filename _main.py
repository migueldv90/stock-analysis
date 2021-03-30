import datetime
from ticker.analysis import analysis


from lists.etfs import tickers as etfs
from lists.crypto import tickers as crypto
from lists.stocks import tickers as stocks
from lists.webull import tickers as webull


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


time_period_30d = '30d'
time_interval_30m = '30m'


time_period_200d = '200d'
time_interval_1d = '1d'


analysis_tickers = webull
scan_tickers = stocks + crypto + etfs


main(time_period_30d, time_interval_30m)
main(time_period_200d, time_interval_1d)
