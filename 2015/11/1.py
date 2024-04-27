import string
letters = string.ascii_lowercase
input = 'hxbxwxba'

def updatePw(pw):
    pw = list(pw)
    for i in range(len(pw), 0, -1):
        if pw[i-1] == 'z':
            pw[i-1] = 'a'
            continue
        else:
            pw[i-1] = letters[letters.index(pw[i-1]) + 1]
            return ''.join(pw)

def checkPw(pw):
    count = 0
    for i in range(len(pw) - 2):
        index = letters.index(pw[i])
        if pw[i:i+3] == letters[index:index + 3]: count += 1
    if count == 0: return False

    if pw.find('i') != -1 or pw.find('o') != -1 or pw.find('l') != -1: return False

    count = []
    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1] and i - 1 not in count: count.append(i)
    if len(count) < 2: return False

    return True

while not checkPw(input):
    input = updatePw(input)
print(input)

