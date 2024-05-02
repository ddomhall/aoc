from copy import deepcopy
input = [list(x) for x in open('input.txt').read().splitlines()]

def get_neighbours(x, y, copy):
    if x == 0 and y == 0:
        neighbours = copy[y][x+1] + copy[y+1][x] + copy[y+1][x+1]
    elif x == len(copy[0]) - 1 and y == 0:
        neighbours = copy[y][x-1] + copy[y+1][x-1] + copy[y+1][x]
    elif x == 0 and y == len(copy) - 1:
        neighbours = copy[y-1][x] + copy[y-1][x+1] + copy[y][x+1]
    elif x == len(copy[0]) - 1 and y == len(copy) - 1:
        neighbours = copy[y-1][x-1] + copy[y-1][x] + copy[y][x-1]
    elif y == 0:
        neighbours = copy[y][x-1] + copy[y][x+1] + copy[y+1][x-1] + copy[y+1][x] + copy[y+1][x+1]
    elif x == 0:
        neighbours = copy[y-1][x] + copy[y-1][x+1] + copy[y][x+1] + copy[y+1][x] + copy[y+1][x+1]
    elif y == len(copy) - 1:
        neighbours = copy[y-1][x-1] + copy[y-1][x] + copy[y-1][x+1] + copy[y][x-1] + copy[y][x+1]
    elif x == len(copy[0]) - 1:
        neighbours = copy[y-1][x-1] + copy[y-1][x] + copy[y][x-1] + copy[y+1][x-1] + copy[y+1][x]
    else:
        neighbours = copy[y-1][x-1] + copy[y-1][x] + copy[y-1][x+1] + copy[y][x-1] + copy[y][x+1] + copy[y+1][x-1] + copy[y+1][x] + copy[y+1][x+1]
    return neighbours.count('#')

for step in range(100):
    ref = deepcopy(input)
    for y in range(len(input)):
        for x in range(len(input)):
            input[y][x] = '#' if (input[y][x] == '#' and get_neighbours(x, y, ref) in [2, 3]) or (input[y][x] == '.' and get_neighbours(x, y, ref) == 3) else '.'

count = 0
for row in input:
    count += row.count('#')
print(count)
