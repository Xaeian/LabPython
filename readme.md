

## Schedule

- Podstawy
  - [x] Typy
  - [x] Instrukcje warunkowe `if`, `match`
  - [x] Pętle `for`, `while`
  - [x] Funkcje
  - [x] Klasy
  - [ ] Moduły zewnętrzne
  - [ ] Operacje na łańcuchach znaków
- Praca z danymi
  - [ ] Metody wprowadzania danych
  - [ ] Pliki **txt**, **json**, **csv**, **ini**
  - [ ] Komunikacja z **api**
  - [ ] Bazy danych **sql**
  - [ ] Biblioteka **pandas** `pd`
  - [ ] Biblioteka **numpy** `np`
  - [ ] Wykresy **matplotlib** `plt`
  - [ ] Notebook **jupyter** `ipynb`
- Komunikacja z urządzeniami zewnętrznymi
  - [ ] Serial port
  - [ ] Modbus RTU
  - [ ] Mikrokontrolery **STM32**
- Aplikacje okienkow GUI
  - [ ] Moduł **Tkinter**
  - [ ] Biblioteka **Eel**
- Aplikacje webowe
  - [ ] Środowisko wirtualne **`venv`**
  - [ ] Framework **flask**

# Podstawy

Funkcja `print` jest jedną z maginczych funkcji w języku **Python**, do któej możesz włożyć wszystko.
Na początek nie zakszodzi włożyć łańcuch znaków `string`

```py
print("Hello world!")
```

Oto wszystkie natwyne **typy** _(klasy)_:

```py
myint = 69
myint2 = -11
myfloat = 2.43
myfloat2 = -7.
mystr = "xyz"
mychar = 'g'
mybool = True
mynull = None
mylist = ["triumvirate", -60, -43]
mytuple = (21, 37, "kremowka")
mydict = { "name": "Edward", "age": 13, "likePancakes": False }
# Łączy w pary wartości, gdzie klucz wskazuje na wartość
```

Krotki `tuple` i Listy `list` są elementami _"tablicowymi"_. Obie mogą zawierać różne typy. Listy możemy  swobodnie edytować w odróżnieniu od krotek, które stanową _"jakby"_ jedną wartość, którą możemy zmienić tylko jako całość. Słowkik `dict` Łączy w pary wartości, gdzie klucz `key` wskazuje na wartość `value`. Jest takim _"obiektem standardowym"_ z innych języków. Wszystkie typy złożone można dowolnie zagnieżdzać.

```py
hero = {
  "stats": { "str": 12, "dex": 4, "int": 7 },
  "eq": ["sword", "bow", "armor"],
  "skils": ("frenzy", "charge"),
  "gold": 35
}
```

Mimo, że nie wskazujemy typów zmiennych to interpreter _"domyśla się"_ oraz na sztywno nadaje typy.

```py
print(myint, type(myint))
print(myint2, type(myint2))
print(myfloat, type(myfloat))
print(myfloat2, type(myfloat2))
print(mystr, type(mystr))
print(mychar, type(mychar))
print(mybool, type(mybool))
print(mynull, type(mynull))
print(mylist, type(mylist))
print(mytuple, type(mytuple))
print(mydict, type(mydict))
```

I co za tym idzie trzeba wykonywać jawne konwersje. Nazwa typu jest również funkcją próby zamiany na wskazany typ. Jak w przykładzie...

```py
print("myint: " + str(myint))
print(myfloat, int(myfloat))
```

### Instrukcje warunkowe

Podstawowa konstrukcja `if else` może wyglądać w ten sposób

```py
# age = ...something
if age == "" or age is None:
  print("Error: Age not specified")
elif age < 0:
  print("Warning: You must be born to progress through this ifs labyrinth")
else:
  if age > 18 and age < 65 and age != 40:
    print("You should work hard")
  else:
    print("You can take care of yourself")
```

Dodatkowy dyspojumeny skróconą składa `if else`, która pozwala zawrzeć nam kilka warównów w jednej linii

```py
# age = ...something
print("Your favorite drink is ...")
print("beer") if age > 18 else print("cola") if age > 2 else print("milk")
```

Od niedawna _(wersja 3.10)_ dysponujemy możliwością używania `switch case`, a właściwie `match case`

```py
# lang = ...your best programming language
print("You can become a ...")
match lang:
  case "javascript":
    print("web developer")
  case "python":
    print("data scientist")
  case "php":
    print("backend developer")
  case "c" | "c++":
    print("embedded system engineer")
  case "kotlin":
    print("mobile app developer")
  case _:
    print("low-skilled physical worker")
```

### Pętla `for`

Działanie pętli `for` w języku Python nieco inaczej niż możemy się spodziewać. Kopiuje ona do zmiennej tymczasowej (zmiennych tymczasowych) kolejne wartości z **objektów iterowalyuch**, do których należą:

- listy - `list`
- krotki - `typle`
- słowniki - `dict`
- inne obiekty sworzone na podstawie klas _(ale nie wszystkie)_

Gdy chcemy po prostu wykonać pewną operację `n` razy najlepiej użyć stwrzyć object **`range`** i przejechać go przętlą `for`.

```py
# range(start, stop, step)
r1 = range(3) # 0 1 2
r2 = range(4, 8) # 4 5 6 7
r3 = range(2, 16, 4) # 2 6 10 14
print(list(r1), tuple(r2), list(r3))
# >> [0, 1, 2] (4, 5, 6, 7) [2, 6, 10, 14]
```

```py
for i in range(5):
  print("nbr:", i)
# >> nbr: 0
# >> nbr: 1
# >> nbr: 2
# >> nbr: 3
# >> nbr: 4
```

Z typami **`tuple`**, **`list`** oraz pętlą `for` prcuje się w ten sam sposób. Wożemy wykonać pętle gdzie pobieramy kolejne elementy listy bądź krotki:

```py
array = (21, 37, "kremowka")
# array = [21, 37, "kremowka"]
for value in array:
  print("value:", value)
# >> value: 21
# >> value: 37
# >> value: kremowka
```

Możemy ponumerować sobie ich elementy funkcją **`enumerate`**. Dzięki temu dodatkowo otrzymamy indeksy elementów:

```py
for i, value in enumerate(array):
  print(i, value, array[i])
# >> 0 21 21
# >> 1 37 37
# >> 2 kremowka kremowka
```

W pracy z typami iterowalymi warto znać funkcję **`len`**. 
W kontekście `for` możemy wykonać liczba iteracji skorelowaną z długością np. listy. Można to wykorzystać, gdy odnosimy się do sąsiednich elementów w liście:

```py
for i in range(len(array)):
  if(i): print(array[i-1])
  else: print(array[0])
# >> kremowka
# >> 21
# >> 37
```

Możemy również pracować z kilkoma listami równocześnie, logicznie je łącząc za pomocą funkcji **`zip`**. Przykładowo możemy nadać własne indeksy:

```py
indexABC = ("a", "b", "c")
for abc, value in zip(indexABC, array):
  print(abc, value)
# >> a 21
# >> b 37
# >> c kremowka
```

```py
indexXYZ = ("x", "y", "z")
for abc, xyz, value in zip(indexABC, indexXYZ, array):
  print(abc, xyz, value)
# >> a x 21
# >> b y 37
# >> c z kremowka
```

Traz przelikePancakestestujmy pętlę `for` na słowniku **`dict`**:

```py
mydict = {
  "name": "Edward",
  "age": 13,
  "likePancakes": False
}
for some in mydict:
  print("some: "some)
# >> some: name
# >> some: age
# >> some: likePancakes
```

Widzimy, że w każdej iteracji został zwrócony nam jedynie klucz `key`. Żeby doprać się do wartości `value` można oczwiście użyć go na obiekcie: 

```py
for key in mydict:
  print(key + ":", mydict[key])
# >> name: Edward
# >> age: 13
# >> likePancakes: False
```

Ale można postępować bardziej elegancko 🧐

```py
for some in mydict.items():
  print(some)
# >> ('name', 'Edward')
# >> ('age', 13)
# >> ('likePancakes', False)

for key, value in mydict.items():
  print(key + ":", value)
# >> name: Edward
# >> age: 13
# >> likePancakes: False
```

Na koniec zostały łańcuchy znaków. Tutaj iteracje zwracają kolejne litery łańcucha `str`:

```py
mystr = "xyz"
for char in mystr:
  print("char:", char)
# char: x
# char: y
# char: z

mystr = "xyz"
for i, char in enumerate(mystr):
  print("char", i, "is", char)
# >> char 0 is x
# >> char 1 is y
# >> char 2 is z
```


<!-- ```py
def sum(x, y):
  return x + y

def sum(*args):
  suma = 0
  for x in args:
    suma += x
  return suma

z = sum(8, 5, 2, 3, 5, 1)
print(z)


def print_keyvalue(**kvargs):  
  for key, value in kvargs.items():
    print(key, value)

print_keyvalue(core=4, cpu="intel")

def str_keyvalue_args(*args, **kvargs):
  txt = "values: "
  for value in args:
    txt += str(value) + " "
  
  txt += "\nkv: "
  for key, value in kvargs.items():
    txt +=  str(key) + ":" + str(value) + " "
  return txt

txt = str_keyvalue_args(2, 3, 4, "aaaa", "ddaas", core=4, cpu="intel")
print(txt)

def avg_scale(values, scales):
  top, bot = 0, 0
  for value, scale in zip(values, scales):
    top += value * scale
    bot += scale
  return top / bot
  
print(avg_scale([3, 4, 4, 5, 3], [1, 1, 2, 8, 1]))
```



Pętla `while` wynonuje w kółk swoją zawartość dopuki warunek jest prawdą `True`.

```py
n = 0
while n < 10:
  print(n)
  n += 1
```

```py
n = 0
while True:
  if(n > )
  print(n)
```


```py
for char in mystr:
  print(char)
``` -->
