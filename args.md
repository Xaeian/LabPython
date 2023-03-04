# Arguments [➥](./readme.md)

🥉 Napisz skrypt, który pobiera od użytkownika współczynniki `a`, `b`, `c` _funkcji kwadratowej_ przy pomocy funkcji `input()` oraz zwraca pierwiastki równania. Zwróć uwagę, że dla `a == 0` funkcję trzeba potraktować jak liniową, a jak dodatkowo `b == 0` funkcja będzie stała.

```py
import math

print("a:")
a = float(input())
print("b:")
b = float(input())
print("c:")
c = float(input())

if a == 0:
  if b == 0:
    if c == 0: print(f"Funkcja stała, nieskończenie wiele pierwiastków")
    else: print(f"Funkcja stała, brak pierwiastków")
  else:
    x = -c/b
    print(f"Funkcja lioniowa, x = {x}")
else:
  delta = b * b - (4 * a * c)
  if delta < 0:
    print("Funkcja kwadratowa, brak pierwiastków")
  elif delta == 0:
    x = -b / (2 * a)
    print(f"Funkcja kwadratowa, x = {x}")
  else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Funkcja kwadratowa, x1 = {x1}, x2 = {x2}")
```

🥉 Pobierz współczynniki jako argumenty `argv` podczas uruchamiania skryptu przy pomocy modułu `sys`. Po `import sys` argumenty będą dostępne pod `sys.argv`.

```py
import sys

print("arg:", sys.argv)
if len(sys.argv) != 4:
  exit("err: Incorrect number of arguments")

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

print("abc:", a, b, c)
# Calc equation roots
```

🥈 Stwórz predefiniowany łańcuch znaków `str` w formacie `ax^2 + bx + c`. Za pomocą różnych sztuczek manipulacji `string`'ami dobierz się do parametrów `a`, `b`, `c`. Docelowo łańcuch będzie wpisywane przez użytkownika zatem przygotuj się na różnego rodzaju niejednoznaczności 🥳

```py
fstr = "4.48x^2 +6.92X- 21.37"
fstr = fstr.lower()
fstr = fstr.replace(" ","").replace("+"," +").replace("-"," -")
if fstr[1] != "+" and fstr[1] != "-": fstr = "+" + fstr
a, b, c = 0., 0., 0.
for some in fstr.split():
  if "x^2" in some: a = float(some.replace("x^2", ""))
  elif "x" in some: b = float(some.replace("x", ""))
  else: c = float(some)
print("abc:", a, b, c)
# Calc equation roots
```

Zapewnij dowolność w przekazaniu argumentów przy pomocy biblioteki `argparse`.

🥇 Wykorzystaj populatną konwencję, gdzie można agrumenty przekazywać w dowolnej kolejności za pomocą słów kluczwych rozpoczynających się `--` lub sktórów `-`. Przykładowe zapytanie przekazujące `ip` oraz `port` z flagami `print` i `fast`.

```bash
py main --ip 127.0.0.1 --port 7000 --fast --print
py main -i 127.0.0.1 -p 7000 -f -p
py main -i 127.0.0.1 -p 7000 -fp
```

```py
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--string', help='Function in string')
parser.add_argument('-a', type=float,  help='Factor a')
parser.add_argument('-b', type=float, help='Factor b')
parser.add_argument('-c', type=float, help='Factor c')
args = parser.parse_args()

a, b, c = 0., 0., 0.

if args.string:
  fstr = args.string
  fstr = fstr.lower()
  fstr = fstr.replace(" ","").replace("+"," +").replace("-"," -")
  if fstr[1] != "+" and fstr[1] != "-": fstr = "+" + fstr
  for some in fstr.split():
    if "x^2" in some: a = float(some.replace("x^2", ""))
    elif "x" in some: b = float(some.replace("x", ""))
    else: c = float(some)

if args.a: a = args.a
if args.b: b = args.b
if args.c: c = args.c

print("abc:", a, b, c)
# Calc equation roots
```

```bash
# Example exec
py main.py -s "4.48x^2 +6.92X- 21.37"
py main.py -s 4.48x^2+6.92X-21.37
py main.py -a 4.48 -c -21.37 -b 6.92
py main.py -s 4.48x^2+6.92X-21.37 -a 5.05
```