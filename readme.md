```py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
```

## Podstawy

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

ys = [norm(x, u, a) for u, a in zip([0, 0, 1], [1, 2, 2])]

for y in ys:
  plt.plot(x, y)
```

## Diagnostyka i niezawodność

Funkcje oceny niezawodności

- _`f(t)`_ - Gęstość prawdopodobieństwa
- _`Q(t)`_ - Zawodność
- _`R(t)`_ - Niezawodność
- _`λ(t)`_ - Intensywność uszkodzeń
- _`Λ(t)`_ - Funkcja wiodąca _(skumulowana intensywność uszkodzeń)_

Wyprodukowaliśmy partię testową sterowników PLC oraz czujników temperatury oraz monitorowaliśmy liczby uszkodzonych urządzeń w każdym z kolejnych miesięcy. Liczby uszkodzonych urządzeń z kolejnych miesięcy zostały umieszczone w liście `plc` dla sterowników oraz w liście `temp` dla czujników.

```py
plc = [123, 12, 7, 8, 10, 4, 1, 0, 0, 2, 1, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 2, 7, 12, 10, 18, 20, 20, 12, 50, 180, 80, 110, 43, 63]
temp = [34, 12, 4, 2, 1, 0, 1, 0, 0, 2, 1, 0, 0, 8, 9, 20, 41, 78]
```

### Zadanie 1

Oblicz na podstawie zebranych _(z rynku)_ danych wszystkie funkcje oceny niezawodności.

Kierunek konwersji:

Dane z rynku → _`f(t)`_ → _`Q(t)`_ → _`R(t)`_ → _`λ(t)`_ → _`Λ(t)`_

```py
n = len(plc)
f = plc / np.sum(plc) # funkcja gęstości uszkodzeń
Q = np.zeros(n) # zawodność
```

### Zadanie 2

Zaprojektuj optymalny system złożony ze sterownika PLC i czujnika/czujników oraz wyświetl jego niezawodność w odniesieniu do niezawodności połączenia pojedynczego czujnika ze sterownikiem.

### Zadanie 3

Stwórz klasę, która usprawnie ocenę niezawodności systemów złożonych z znacznie większej ilości obiektów.

<!--

```py
n = len(plc)
f = plc / np.sum(plc) # funkcja gęstości uszkodzeń
Q = np.zeros(n) # zawodność
for i in range(1, n):
  Q[i] = Q[i - 1] + f[i]
R = 1 - Q # niezawodność
l = f / R # intensywność uszkodzeń

L = np.zeros(n) # funkcja wiodąca
# skumulowana intensywność uszkodzeń
for i in range(1, n):
  L[i] = L[i - 1] + l[i]
```

```py
n2 = len(temp)
f2 = temp / np.sum(temp)
Q2 = np.zeros(n2)
for i in range(1, n2):
  Q2[i] = Q2[i - 1] + f2[i]
R2 = 1 - Q2
l2 = f2 / R2
```

```py
l3 = l[0:36]
l4 = np.array(list(l2[0:12]) + list(l2[0:12]) + list(l2[0:12]))
plt.plot(l3)
plt.plot(l4 * l4)
l5 = 1 - ((1 - (l4 * l4)) * (1 - l3))
plt.plot(l5)
plt.ylim(0, 0.1)
plt.show()
````

-->
