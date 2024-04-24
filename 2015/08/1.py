text = open('input.txt').read().strip().split('\n')
# text = r'''
# ""
# "abc"
# "aaa\"aaa"
# "\x27"
# '''.strip().split('\n')

count = 0
for line in text:
    count += len(line) - len(eval(line))
print(count)
