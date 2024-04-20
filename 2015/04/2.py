import hashlib

text = open('input.txt').read().strip()

num = 0
while True:
    if hashlib.md5((text + str(num)).encode()).hexdigest().startswith('000000'):
        break
    num += 1

print(num)

