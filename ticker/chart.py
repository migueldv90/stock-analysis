import matplotlib.pyplot as plt


plt.figure(figsize=(15, 2), dpi=120, facecolor='w', edgecolor='k')
plt.plot(x_data, y_data, 'o', markersize=1.5, color='grey', alpha=0.7)
plt.plot(x, y_pol, '-', markersize=1.0, color='black', alpha=0.9)
plt.plot(x[l_min], y_pol[l_min], "o", label="min", color='r')
plt.plot(x[l_max], y_pol[l_max], "o", label="max", color='b')
plt.show()
