text = open('input.txt', 'r').read()
floor = 0

for c in range(len(text)):
    if text[c] == '(':
        floor += 1
    elif text[c] == ')':
        floor -= 1
    if floor == -1:
        print(c+1)
        break

