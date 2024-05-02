input = [list(x) for x in open('input.txt').read().splitlines()]
input = [list(x) for x in open('test_input.txt').read().splitlines()]
print(input)

def get_neighbours(x, y, copy):
    return 0

for step in range(1):
    ref = input.copy()
    for y in range(len(input)):
        for x in range(len(input)):
            if input[y][x] == '#':
                if get_neighbours(x, y, ref) in [2, 3]:
                    input[y][x] = '#'
                else:
                    input[y][x] = '.'
            else:
                if get_neighbours(x, y, ref) == 3:
                    input[y][x] = '#'
                else:
                    input[y][x] = '.'

print(input)
