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

### Zadanie 3

Stwórz klasę, która usprawni ocenę niezawodności systemów złożonych z znacznie większej ilości obiektów oraz za jej pomocą zrealizuj poprzednie zadanie.
Na podstawie tej klasy zostaną stworzone obiekty `plc` _(sterownik PLC)_ oraz `temp` _(czujnik temperatury)_
