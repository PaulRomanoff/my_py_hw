# CW_tasks_testing
# 6.1
import math as m
print(m.sin(m.pi/2))
print(m.pi)
for el_name in dir(m):
    print(el_name, end="\t")
print("\n")

# 6.2
ad = 90
ar = m.radians(ad)
ad = m.degrees(ar)
print("1)", ad == 90.)
print("2)", ar == m.pi / 2.)
print("3)", m.sin(ar) / m.cos(ar) == m.tan(ar))
print("4)", m.asin(m.sin(ar)) == ar)
print("5)", m.pow(m.e, 1) == m.exp(m.log(m.e)))
print("6)", m.factorial(5))
print("\n")

# 6.3
from random import random, seed, randrange, randint, choice, sample

for i in range(5):
    print(random())
print("\n")

seed(7)
for i in range(3):
    print(random())
for i in range(3):
    print(randrange(1,15))
print("\n")

for i in range (10):
    print(randint(1,10), end=", ")
print("\n\n")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))
print(sample(my_list, 5))
print("\n")

# 6.4
from platform import platform, machine, processor, system, version, python_version
print(system())
print(platform(1))
print(version())
print(machine())
print(processor())
print(python_version())