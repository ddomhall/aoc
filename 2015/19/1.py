input = [x.split(' => ') for x in open('input.txt').read().splitlines() if x]
start = ''.join(input.pop(-1))

molecules = set()
for i in range(len(start)):
    for replacement in input:
        if (len(replacement[0]) == 1 and start[i] != replacement[0]) or (len(replacement[0]) == 2 and start[i:i+2] != replacement[0]): continue
        molecules.add(start[:i] + replacement[1] + start[i+len(replacement[0]):])

print(len(molecules))
