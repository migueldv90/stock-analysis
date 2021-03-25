import numpy as np


def highlow(data):
    x_data = list(range(data.index.size))
    y_data = data['Low']

    x = np.linspace(0, max(x_data), max(x_data) + 1)

    x_pol = np.polyfit(x_data, y_data, 80)
    y_pol = np.polyval(x_pol, x)

    min_max = np.diff(np.sign(np.diff(y_pol))).nonzero()[0] + 1
    l_min = (np.diff(np.sign(np.diff(y_pol))) > 0).nonzero()[0] + 1
    l_max = (np.diff(np.sign(np.diff(y_pol))) < 0).nonzero()[0] + 1
