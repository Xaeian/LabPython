Main.py

```py
import file
import pandas as pd

data = file.csv_load_data("data.csv")
print(data)

df = pd.read_csv('data.csv')
print(df)
```

File.py

```py
import csv, codecs, json
import json

def csv_load(path:str, delimiter:str=",") -> list:
  return list(csv.DictReader(codecs.open(path, "r", "utf-8")))

def csv_load_data(path:str, delimiter:str=",") -> list:
  data = csv_load(path, delimiter)
  keys = list(data[0].keys())
  series = {}
  for key in keys:
    series[key] = []
  for row in data:
    for key in keys:
      series[key] += [row[key]]
  return series
```