from functools import reduce
from math import sqrt

input = 36000000
house = 1

def factors(n) :
    step = 2 if n%2 else 1
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

while True:
    if sum([n*10 for n in factors(house)]) >= input:
        break
    else:
        house += 1

print(house)

