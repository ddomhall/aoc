text = open('input.txt').read().strip().split('\n')

grid = [[False for _ in range(1000)] for _ in range(1000)]

for line in text:
    line = line.split()
    if line[0] == 'turn':
        line = [line[1]] + [[int(x) for x in line[2].split(',')]] + [[int(x) for x in line[4].split(',')]]
    else:
        line = [line[0]] + [[int(x) for x in line[1].split(',')]] + [[int(x) for x in line[3].split(',')]]

    for i in range(int(line[1][1]), int(line[2][1]) + 1):
        for j in range(int(line[1][0]), int(line[2][0]) + 1):
            match line[0]:
                case 'on':
                    grid[i][j] = True
                case 'off':
                    grid[i][j] = False
                case 'toggle':
                    grid[i][j] = not grid[i][j]

count = 0
for row in grid:
    for item in row:
        if item: count += 1

print(count)
