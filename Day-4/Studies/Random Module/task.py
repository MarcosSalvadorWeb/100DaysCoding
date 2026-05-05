import random as rnd
from random import uniform

import my_module

number = rnd.randint(0, 100)
print(f"número inteiro {number}")

real_number = rnd.random()*100
print(f"número real {real_number}")

uniform_number = rnd.uniform(0, 100)
print(f"número uniforme {uniform_number}")

if uniform_number > 50:
    print("Heads")
else :
    print("Tails")

print(my_module.hey)
