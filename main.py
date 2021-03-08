import threading
from stock import ticker_analysis


def main():
    threading.Timer(5, main).start()

    file = open('tickers.txt', 'w')
    for ticker in tickers:
        ticker_analysis(ticker, file)
    file.close()


tickers = ['flux', 'gevo', 'mu', 'jmia', 'baba', 'tigr', 'nndm', 'dm', 'csiq', 'lndc', 'lazr', 'idex', 'nio', 'riot', 'mara', 'mmm']
main()
