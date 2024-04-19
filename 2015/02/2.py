text = open('input.txt', 'r').read().split()
sum = 0

for i in text:
    l, w, h = map(int, i.split('x'))
    m1, m2, m3 = sorted([l, w, h])
    sum += l*w*h + 2*m1 + 2*m2

print(sum)

