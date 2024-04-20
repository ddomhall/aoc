text = open('input.txt').read()

coords = [0, 0]
visited = set(['0, 0'])

for c in text:
    match c:
        case '^':
            coords[1] += 1
        case '>':
            coords[0] += 1
        case 'v':
            coords[1] -= 1
        case '<':
            coords[0] -= 1
    visited.add(f'{coords[0]}, {coords[1]}')

print(len(visited))

