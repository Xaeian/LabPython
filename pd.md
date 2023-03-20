# Pandas, Signals [➥](./readme.md)

🥉 Wczytaj plik z danymi [`data.csv`](./data.csv). Znajdują się w nim pomiary z akcelerometru w osiach **x**, **y**, **z** wykonywane z częstotliwością **6666Hz**. Dadaj na początek kołomęt czasu oraz na koniec kolumnę z przyspieszeniem wypadkowym oraz zapisz całość jako nowy plik `csv` 🚫🐼

🥈 Oblicz **FFT** dla wszystkich osi, a wyniki zaprezentuj na wykresie oraz zapisz je do pliku. Napisz fragment kodu, który znajduje częstotliwość wiodącą 👍🐼

```py
fs = 6666 # częstotliwość próbkowania
window = np.hamming(len(serie)) # okno czasowe
fft = np.abs(np.fft.rfft(serie * window)) # wartość FFT
freq = np.fft.rfftfreq(len(serie), 1 / fs)
# częstotliowści dla FFT
```

🥇 Dodaj do naszego sygnału zakłócenia na poziomie **~10%** amplitudy `amp` sygnału, a następnie odfiltruj częstotliwość wiodącą za pomocą filtru pasmowoprzepustowego

```py
noise = np.random.normal(-amp, amp, len(serie))
serie = serie + noise
# dodanie szumu
fnyquist = fs / 2
low = flow / fnyquist
high = fhigh / fnyquist
b, a = butter(order, [low, high], btype='band')
# projektowanie filtru
serie = lfilter(b, a, serie)
# filtraacja
```
