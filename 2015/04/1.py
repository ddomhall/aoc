import hashlib

text = open('input.txt').read().strip()

print(text)

num = 0
while True:
    if hashlib.md5((text + str(num)).encode()).hexdigest().startswith('00000'):
        break
    num += 1

print(num)
