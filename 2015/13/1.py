from itertools import permutations 
input = open('input.txt').read().splitlines()

seats = dict()
for row in input:
    user1, _, diff, value, _, _, _, _, _, _, user2 = row.rstrip('.').split()
    seats.setdefault(user1, dict())[user2] = int(value) if diff == 'gain' else - int(value)

happiness = 0
for pattern in permutations(seats):
    total = 0
    for i in range(len(pattern)):
        name = pattern[i]
        if i == 0:
            total += seats[name][pattern[i + 1]] + seats[name][pattern[-1]]
        elif i == len(pattern) - 1:
            total += seats[name][pattern[0]] + seats[name][pattern[i - 1]]
        else:
            total += seats[name][pattern[i + 1]] + seats[name][pattern[i - 1]]
    if total > happiness: happiness = total

print(happiness)
