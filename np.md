# Numpy, Matplotlib [➥](./readme.md)

🥉 Napisz program, który oblicza [rozkład normalny _(Gaussa)_](https://pl.wikipedia.org/wiki/Rozk%C5%82ad_normalny) dla zadanych przez użytkownika parametrów. Należą do nich:

- odchylenie standardowe _**σ**_ albo wariacja _**σ²**_
- średnia rozkładu _**µ**_
- przedział dla obliczeń _〈**min**,**max**〉_

Wynik zaprezentuj na wykresie. _Nie używaj modułów zewnętrznych poza `numpy` oraz `matplotlib`._

🥈 Porównaj własną implementację rozkładu normalnego z funkcją wbudowaną w `scipy.stats` na dwych wykresach przy pomocy `subplots`.

🥇 Zapewnij użytkownikowi możliwość wprowadzania różnych konfiguracji parametrów _**σ**_/_**σ²**_ oraz _**µ**_ poprzez wykorzystanie argumentów.

```bash
# Example exec
py main.py -s 1.5 -u 4 --min -10 --max 10
py main.py -w 2.25 -u 4 -r -10 10
py main.py -s 1 1.5 2 -u 4
py main.py -s 1.5 -u 3 4 5
# -s: odchylenie standardowe
# -u: średnia
# -w: wariacja
# -r: przedział (range)
```