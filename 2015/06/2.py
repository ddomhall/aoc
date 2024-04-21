text = open('input.txt').read().strip().split('\n')

grid = [[0 for _ in range(1000)] for _ in range(1000)]

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
                    grid[i][j] += 1
                case 'off':
                    if grid[i][j] > 0: grid[i][j] -= 1
                case 'toggle':
                    grid[i][j] += 2

count = 0
for row in grid:
    for item in row:
        count += item

print(count)

