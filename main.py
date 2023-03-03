import sys

# print(sys.argv)

import argparse

# run -i -f
# run -if
# run --install --fast

# py main.py -s "3.4x^2 +2.1X- 12"
# py main.py -s 3.4x^2+2.1X-12
# py main.py -a 3.4 -c -12 -b 2.1

# py main.py -s 3.4x^2+2.1X-12 -a 1.12

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

print(a, b, c)
