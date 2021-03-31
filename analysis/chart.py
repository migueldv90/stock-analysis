import matplotlib.pyplot as plt


plt.figure(figsize=(15, 2), dpi=120, facecolor='w', edgecolor='k')
plt.plot(x_data, y_data, 'o', markersize=1.5, color='grey', alpha=0.7)
plt.plot(x, y_pol, '-', markersize=1.0, color='black', alpha=0.9)
plt.plot(x[l_min], y_pol[l_min], "o", label="min", color='r')
plt.plot(x[l_max], y_pol[l_max], "o", label="max", color='b')
plt.show()


import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2)


ax1.plot(df.index, ten_ema, label='FB MACD', color='blue')
ax1.plot(df.index, ten_sma, label='Signal Line', color='red')
ax1.legend(loc='upper left')

ax2.plot(df.index, MACD, label='FB MACD', color='blue')
ax2.plot(df.index, signal, label='Signal Line', color='red')
ax2.legend(loc='upper left')

plt.show()
