```py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
```

```py
x = np.linspace(start=0, stop=10, num=100)
y = np.arange(start=0, stop=10, step=0.1)
```

```py
u = 5
a = 1

y1 = stats.norm.pdf(x, u, a)
y2 = (1 / (a * np.sqrt(2 * np.pi))) * np.exp((-np.power(x-u, 2))/(2 * np.power(a, 2))); # generowanie przebiegu gaussa

plt.subplot(211)
plt.plot(x, y1)
plt.subplot(212)
plt.plot(x, y2)
```

```py
x = np.linspace(start=-5, stop=15, num=100)

def norm(x, u, a):
  return (1 / (a * np.sqrt(2 * np.pi))) * np.exp((-np.power(x-u, 2))/(2 * np.power(a, 2)))

u = 5
ys = [norm(x, u, a) for a in [1, 2, 3]]

for y in ys:
  plt.plot(x, y)
```