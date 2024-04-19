text = open('input.txt', 'r').read().split()
sum = 0

for i in text:
    l, w, h = map(int, i.split('x'))
    sum += 2*l*w + 2*w*h + 2*h*l + sorted([l, w, h])[0]*sorted([l, w, h])[1]

print(sum)
