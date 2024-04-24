import re
text = open('input.txt').read().strip().split('\n')
# text = r'''
# ""
# "abc"
# "aaa\"aaa"
# "\x27"
# '''.strip().split('\n')

count = 0
for line in text:
    count+= len(re.escape(line)) + len(re.findall('"', line[1:-1])) + 4 - len(line)
print(count)
