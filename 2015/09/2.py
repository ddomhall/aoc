from itertools import permutations 

text = open('input.txt').read().strip().split('\n')
# text = open('test_input.txt').read().strip().split('\n')

places = set()
routes = dict()
for line in text:
    (start, _, end, _, distance) = line.split()
    places.add(start)
    places.add(end)
    routes.setdefault(start, dict())[end] = int(distance)
    routes.setdefault(end, dict())[start] = int(distance)

length = 0
for path in permutations(places):
    sum = 0
    for i in range(len(path) - 1):
        sum += routes[path[i]][path[i+1]]
    if sum > length:
        length = sum

print(length)

