## Zadania

- **1** Napisz skrypt, który pobiera program od użytkownika parametry  współczynniki `a`, `b`, `c` funkcji kwadratowej przy pomocy funkcji `input()` oraz zwraca pierwiastki równania. Zwróć uwagę, że dla `a == 0` funkcję trzeba potraktować jak liniową, a jak dodatkowo `b == 0` funkcja będzie stała.
  - Pobierz współczynniki jako argumenty `argv` podczas uruchamiania skryptu przy pomocy modułu `sys`
  - Pobierz od użytkownika łańcuch znaków `str` w formacie `ax^2 + bx + c`. Za pomocą różnych sztuczek manipulacji `string`'ami dobierz się do parametrów `a`, `b`, `c`
  - Zapewnij dowolność w przekazaniu argumentów przy pomocy biblioteki `argparse`