import numpy as np
import matplotlib.pyplot as plt
a, m = 3., 1. 
s = np.random.pareto(a, 1000) + m
count, bins, ignored = plt.hist(s, 100, normed=True)
fit = a*m**a/bins**(a+1)
plt.plot(bins, max(count)*fit/max(fit),linewidth=2, color='r')
plt.show()
