import itertools
from sys import maxsize
input = [int(x) for x in open('input.txt').read().splitlines()]

combinations = []
for i in range(1,len(input)):
    for s in itertools.combinations(input,i):
        if sum(s)==150: combinations.append(s)

min = maxsize
count = 0
for i in combinations:
    if len(i) < min:
        min = len(i)
        count = 1
    elif len(i) == min: count += 1

print(count)

