text = open('input.txt', 'r').read()

floor = 0

for c in text:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1

print(floor)
