"""
import random

#r = random.randint(0, 2)
#r = random.uniform(0, 1)
r = random.randrange(3)
print(r)
"""
import random


a = random.randrange(0, 50, 5)
b = random.randrange(0, 50, 5)

print(f"a: {a} et b: {b}")
if a < b:
    print("Le nombre b est plus grand que le nombre a.")
elif a > b:
    print("Le nombre a est plus grand que le nombre b.")
else:
    print("Le nombre a et le nombre b sont égaux.")