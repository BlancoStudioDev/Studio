import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom

p = 0.5
n = 3
x = np.arange(0, 10)
y = binom(n, x) * p**x * (1 - p) ** (n - x)
plt.bar(x, y)
plt.show()

r = 35
o = 40
p = 0.2

x = np.arange(0, o * r + 1)
y = binom(o, x / r) * p ** (x / r) * (1 - p) ** (o - x / r)
plt.bar(x, y)
plt.show()
