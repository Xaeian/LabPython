from database import Database

conn = Database("iot", "localhost", "root", "sqrt")

# TODO Device {id} form argument
ID = 1

array = conn.getArray(f"SELECT time, temperature, humidity, voltage FROM data WHERE device_id = {ID}")

# for row in array:
#   print(row)

# TODO Transponowanie tablicy
# TODO Wyśiwetlanie matplotlib (subplotes)

