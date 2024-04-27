input = [int(c) for c in '1321131112']

def expand(input):
    output = []
    count = 1
    for i in range(len(input)):
        if i == len(input) - 1 or input[i] != input[i + 1]:
            output.extend([count, input[i]])
            count = 1
        else:
            count += 1
    return output

for i in range(50):
    input = expand(input)

print(len(input))


