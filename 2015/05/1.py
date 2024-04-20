text = open('input.txt').read().split()
nice = 0

for i in text:
    count = 0
    for l in i:
        if l in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    if count < 3:
        continue

    count = 0
    for l in range(len(i)):
        if l < len(i) - 1 and i[l] == i[l+1]:
            count += 1
    if count == 0:
        continue

    count = 0
    for s in ['ab', 'cd', 'pq', 'xy']:
        if s in i:
            count += 1
    if count != 0:
        continue

    nice += 1

print(nice)
