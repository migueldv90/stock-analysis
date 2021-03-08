import threading
from stock import ticker_analysis


def main():
    # threading.Timer(5, main).start()

    file = open('tickers.txt', 'w')
    for ticker in tickers:
        ticker_analysis(ticker, file)
    file.close()


tickers = ['dkng', 'penn', 'flux', 'gevo', 'mu', 'jmia', 'tigr', 'nndm', 'dm', 'csiq', 'lazr', 'idex', 'nio',
           'riot', 'mara', 'mmm', 'tan', 'icln', 'arkg', 'arkq', 'arkf', 'arkw', 'arkk', 'qqq', 'spyg', 'spy']
main()
