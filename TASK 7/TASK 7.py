# import user defined module
import module

print(module.l)
module.l = [i - 8 for i in module.l]
print(module.l)

# pandas package
import pandas as p

g = ['g', 'o', 'k', 'u' , 'l']
s = p.Series(g)
print(s)

# random module
import random as r

a = list(range(1, 101))
print(r.choice(a))

# sys package and python path
import sys

for b in sys.path:
   print(b)
