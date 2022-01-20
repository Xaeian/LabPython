```py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
```

```py
x = np.linspace(start=-5, stop=15, num=300)
y = np.arange(start=-5, stop=15, step=0.1)
```

```py
u = 5
a = 1

y1 = stats.norm.pdf(x, u, a)
y2 = (1 / (np.sqrt(2 * np.pi))) * np.exp((-np.power(x-u, 2))/(2 * np.power(a, 2))); # generowanie przebiegu gaussa

plt.subplot(211)
plt.plot(x, y1)
plt.subplot(212)
plt.plot(x, y2)

plt.show()
```