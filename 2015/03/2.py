text = open('input.txt').read()

coords1 = [0, 0]
coords2 = [0, 0]
turn1 = True
visited = set(['0, 0'])

for c in text:
    if turn1:
        match c:
            case '^':
                coords1[1] += 1
            case '>':
                coords1[0] += 1
            case 'v':
                coords1[1] -= 1
            case '<':
                coords1[0] -= 1
        visited.add(f'{coords1[0]}, {coords1[1]}')
    else:
        match c:
            case '^':
                coords2[1] += 1
            case '>':
                coords2[0] += 1
            case 'v':
                coords2[1] -= 1
            case '<':
                coords2[0] -= 1
        visited.add(f'{coords2[0]}, {coords2[1]}')
    turn1 = not turn1

print(len(visited))
