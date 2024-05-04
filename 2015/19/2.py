from random import shuffle
input = [x.split(' => ') for x in open('input.txt').read().splitlines() if x]
end = ''.join(input.pop(-1))

target = end
count = 0

while target != 'e':
    cur = target
    for inp, out in input:
        if out not in target: continue
        target = target.replace(out, inp, 1)
        count += 1

    if cur == target:
        target = end
        count = 0
        shuffle(input)

print(count)
