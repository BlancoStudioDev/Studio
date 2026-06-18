import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = 0.5

x = np.linspace(0, a)
y = (3 / a**2) * x**2 - (2 / a**3) * x**3

plt.plot(x, y)
plt.show()
