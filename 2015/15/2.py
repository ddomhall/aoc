def fint(x):
    return int(x.rstrip(','))

def positive(x):
    return 0 if x < 0 else x

input = [[fint(x[2]), fint(x[4]), fint(x[6]), fint(x[8]), fint(x[10])] for x in [x.split() for x in open('input.txt').read().splitlines()]]

combinations = []
for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            d = 100-a-b-c
            if d > 0: combinations.append([a,b,c,d])

highest = 0
for combination in combinations:
    capacity = positive(combination[0] * input[0][0] + combination[1] * input[1][0] + combination[2] * input[2][0] + combination[3] * input[3][0])
    durability = positive(combination[0] * input[0][1] + combination[1] * input[1][1] + combination[2] * input[2][1] + combination[3] * input[3][1])
    flavor = positive(combination[0] * input[0][2] + combination[1] * input[1][2] + combination[2] * input[2][2] + combination[3] * input[3][2])
    texture = positive(combination[0] * input[0][3] + combination[1] * input[1][3] + combination[2] * input[2][3] + combination[3] * input[3][3])
    calories = positive(combination[0] * input[0][4] + combination[1] * input[1][4] + combination[2] * input[2][4] + combination[3] * input[3][4])
    total = capacity * durability * flavor * texture
    if total > highest and calories == 500: highest = total

print(highest)


