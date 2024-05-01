import itertools
input = [int(x) for x in open('input.txt').read().splitlines()]

combinations = []
for i in range(1,len(input)):
    for s in itertools.combinations(input,i):
        if sum(s)==150: combinations.append(s)

print(len(combinations))
