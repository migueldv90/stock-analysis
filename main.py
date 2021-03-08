import threading
from stock import ticker_analysis


def main():
    # threading.Timer(5, main).start()

    file = open('tickers.txt', 'w')
    for ticker in tickers:
        ticker_analysis(ticker, time_frame, file)
    file.close()


tickers = ['dkng', 'penn', 'flux', 'gevo', 'mu', 'jmia', 'tigr', 'nndm', 'dm', 'csiq', 'lazr', 'idex', 'nio', 'riot', 'mara', 'mmm']
tickers = ['tan', 'icln', 'arkg', 'arkq', 'arkf', 'arkw', 'arkk', 'qqq', 'spyg', 'spy']
tickers = ['btc-usd', 'eth-usd']

time_frame = '1d'


main()
