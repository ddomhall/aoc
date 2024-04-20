text = open('input.txt').read().split()
nice = 0

for i in text:
    found = False
    patterns = {}
    for l in range(len(i)-1):
        try:
            if patterns[i[l] + i[l+1]] != l - 1:
                found = True
        except:
            patterns[i[l] + i[l+1]] = l
    if not found:
        continue

    found = False
    for l in range(len(i)):
        if l < len(i) - 2 and i[l] == i[l+2]:
            found = True
    if not found:
        continue

    nice += 1

print(nice)

