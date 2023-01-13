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

Rozwiązanie:

```py
n = len(plc)

f = plc / np.sum(plc) # funkcja gęstości uszkodzeń

Q = np.zeros(n) # zawodność
for i in range(1, n):
  Q[i] = Q[i] - f[i - 1] if i else f[i]

R = 1 - Q # niezawodność

l = f / R # intensywność uszkodzeń

L = np.zeros(n) # funkcja wiodąca
# skumulowana intensywność uszkodzeń
for i in range(1, n):
  L[i] = L[i] - l[i - 1] if i else l[i]
```

### Zadanie 2

Aby system działa musi sterownik PLC i czujnik muszą być sprawne.
System musi cechować się dużą niezawodnością przez `2 lata`.
Produkty _(PLC, czujnik)_ możesz wprowadzać na rynek po dowolnym czasie testów _(wówczas z listy możesz **usunąć** elementy **początkowe**)_.
Możesz zlecać wymianę produktu _(PLC, czujnik)_ w dowolnym miesiącu _(wówczas z listy możesz **usunąć** elementy **końcowe**, oraz możesz zwielokrotnić dany wektor)
Ostatecznie wektory muszą być tej samej długości.
Możesz stosować redundancje.
Czujnik temperatury stanowi ułamek ceny sterownika PLC.
Oblicz wypadkową funkcję gęstości uszkodzeń _`f(t)`_ całego systemu.
Wyświetl ją na wspólnym wykresie wraz z cząstkowymi funkcjami gęstości uszkodzeń w celu porównania.

W przykładowym rozwiązaniu sterowniki PLC były testowane przez `1 miesiąc`, a czujniki temperatury przez `2 miesiące`
Wymiana czujnika zaplanowana jest na `13 miesiącu` jego pracy _(zatem podczas jednego cyklu życia PLC zużywane będą 3 czujniki)_
Powstałe wektory:

```py
plc_base = [123, 12, 7, 8, 10, 4, 1, 0, 0, 2, 1, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 2, 7, 12, 10, 18, 20, 20, 12, 50, 180, 80, 110, 43, 63]
temp_base = [34, 12, 4, 2, 1, 0, 1, 0, 0, 2, 1, 0, 0, 8, 9, 20, 41, 78]

plc_init = plc_base[1:]
temp_init = 3 * temp_base[2:15]
```

Rozwiązanie:

```py
def df(fnc):
  n = len(fnc)
  res = np.zeros(n)
  for i in range(0, n):
    res[i] = fnc[i] - fnc[i - 1] if i else fnc[i]
  return res

def integral(fnc):
  n = len(fnc)
  res = np.zeros(n)
  for i in range(0, n):
    res[i] = res[i - 1] + fnc[i] if i else fnc[i]
  return res

plc_f = plc / np.sum(plc_init)
temp_f = temp / np.sum(temp_init)

plc_Q = integral(plc_f)
plc_R = 1 - plc_Q

temp_Q = integral(temp_f)
temp_x2_Q = temp_Q**2
temp_x2_f = df(temp_x2_Q)
temp_x2_R = 1 - temp_x2_Q

sys_R = temp_x2_R * plc_R
sys_Q = 1 - sys_R
sys_f = df(sys_Q)

plt.plot(plc_f)
plt.plot(temp_f)
plt.plot(temp_x2_f)
plt.plot(sys_f)
plt.show()
```

### Zadanie 3

Stwórz klasę, która usprawni ocenę niezawodności systemów złożonych z znacznie większej ilości obiektów oraz za jej pomocą zrealizuj poprzednie zadanie.
Na podstawie tej klasy zostaną stworzone obiekty `plc` _(sterownik PLC)_ oraz `temp` _(czujnik temperatury)_

Struktura klasy _(pozbawiona obsługi metod)_

```py
class Reliability:
  def __init__(self, init:list|None):
    if init:
      #self.f = ...
      #self.Q = ...
      #self.R = ...
      pass  
    else:
      self.f, self.Q, self.R = None, None, None
    
  def Parallel(self, conn) -> object:
    new = Reliability()
    #new.f = ...
    #new.Q = ...
    #new.R = ...
    return new
  
  def Series(self, conn) -> object:
    new = Reliability()
    #new.f = ...
    #new.Q = ...
    #new.R = ...
    return new
  
  def Plot(self, param="f"):
    plt.plot(self.R) if param == "R" else plt.plot(self.Q) \
    if param == "Q" else plt.plot(self.f)
```

Wywołanie:

```py
plc = Reliability(plc_init)
temp = Reliability(temp_init)

temp2 = temp.Parallel(temp)
sys = plc.Series(temp2)

plc.Plot()
temp.Plot()
temp2.Plot()
sys.Plot()
plt.show()
```

Struktura klasy:

```py
class Reliability:
  def __init__(self, init:list|None=None):
    if init:
      self.f = init / np.sum(init)
      self.Q = integral(self.f)
      self.R = 1 - self.Q
    else:
      self.f, self.Q, self.R = None, None, None
    
  def Parallel(self, conn) -> object:
    new = Reliability()
    new.Q = self.Q * conn.Q
    new.f = df(new.Q)
    new.R = 1 - new.Q
    return new
  
  def Series(self, conn) -> object:
    new = Reliability()
    new.R = self.R * conn.R
    new.Q = 1 - new.R
    new.f = df(new.Q)
    return new
  
  def Plot(self, param="f"):
    plt.plot(self.R) if param == "R" else plt.plot(self.Q) \
    if param == "Q" else plt.plot(self.f)
```