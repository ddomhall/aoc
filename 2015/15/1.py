input = [{x[1]: int(x[2].rstrip(',')), x[3]: int(x[4].rstrip(',')), x[5]: int(x[6].rstrip(',')), x[7]: int(x[8].rstrip(',')), x[9]: int(x[10].rstrip(',')) } for x in [x.split() for x in open('input.txt').read().splitlines()]]
input = [{x[1]: int(x[2].rstrip(',')), x[3]: int(x[4].rstrip(',')), x[5]: int(x[6].rstrip(',')), x[7]: int(x[8].rstrip(',')), x[9]: int(x[10].rstrip(',')) } for x in [x.split() for x in open('test_input.txt').read().splitlines()]]
input = [[ int(x[2].rstrip(',')), int(x[4].rstrip(',')), int(x[6].rstrip(',')), int(x[8].rstrip(',')), int(x[10].rstrip(',')) ] for x in [x.split() for x in open('input.txt').read().splitlines()]]
input = [[ int(x[2].rstrip(',')), int(x[4].rstrip(',')), int(x[6].rstrip(',')), int(x[8].rstrip(',')), int(x[10].rstrip(',')) ] for x in [x.split() for x in open('test_input.txt').read().splitlines()]]

combinations = []
for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            d = 100-a-b-c
            if d > 0: combinations.append([a,b,c,d])

combinations = []
for a in range(1, 100):
    b = 100-a
    if b > 0: combinations.append([a,b])

'''
combination 0 * inp 0 capacity + combination 1 * inp 1 capacity

combination 0 * inp 0 durability + combination 1 * inp 1 durability

combination 0 * inp 0 flavor + combination 1 * inp 1 flavor

combination 0 * inp 0 texture + combination 1 * inp 1 texture
'''

def positive(x):
    return 0 if x < 0 else x

combinations = [[44 ,56]]
highest = 0
for combination in combinations:
    capacity = positive(combination[0] * input[0][0] + combination[1] * input[1][0])
    durability = positive(combination[0] * input[0][1] + combination[1] * input[1][1])
    flavor = positive(combination[0] * input[0][2] + combination[1] * input[1][2])
    texture = positive(combination[0] * input[0][3] + combination[1] * input[1][3])
    total = capacity * durability * flavor * texture
    if total > highest: highest = total

print(highest)

