text = open('input.txt').read().split('\n')
text = open('test_input.txt').read().split('\n')

values = {}
for row in text:
    row = row.split()
    match len(row):
        case 3:
            if row[0].islower():
                values[row[2]] = values[row[0]]
            values[row[2]] = int(row[0])
        case 4:
            values[row[3]] = values[row[1]] ^ 65535
        case 5:
            match row[1]:
                case 'AND':
                    values[row[4]] = values[row[0]] & values[row[2]]
                case 'OR':
                    values[row[4]] = values[row[0]] | values[row[2]]
                case 'LSHIFT':
                    values[row[4]] = values[row[0]] << int(row[2])
                case 'RSHIFT':
                    values[row[4]] = values[row[0]] >> int(row[2])

print(values)
