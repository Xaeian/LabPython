import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()
root.title()
root.geometry("190x185")

greeting = tk.Label(text="Data viewer")
greeting.pack()

vars = []
for txt in ["Temperatura", "Wilgotność", "Napięcie"]:
  var = tk.IntVar()
  vars.append(var)
  checkbox = tk.Checkbutton(root, text=txt, variable=var, onvalue=True, offvalue=False)
  checkbox.pack()

startbox = tk.Entry()
startbox.pack()
stopbox = tk.Entry()
stopbox.pack()

devs = {
  1: "Magazyn", 
  2: "Biuro",
  3: "Konferencyjna"
}
rdevs = {}
for key, name in devs.items():
  rdevs[name] = key

deviceNames = list(devs.values())
combobox = ttk.Combobox(root, values=deviceNames, state="readonly")
combobox.current(tk.END)
combobox.pack()

def displaySereis():
  for i, var in enumerate(vars):
    print(f"Checkboxe {i}:", str(var.get()))
  start = startbox.get().strip()
  stop = stopbox.get().strip()
  print("Range:", start, stop)
  strdev = combobox.get()
  print("Device:", rdevs[strdev])

btn = tk.Button(root, text ="Wyświetl", command=displaySereis)
btn.pack()

root.mainloop()
