text = open('input.txt').read().strip().split('\n')
# text = open('test_input.txt').read().strip().split('\n')

# values = {}
# for row in text:
#     row = row.split()
#     match len(row):
#         case 3:
#             if row[0].islower():
#                 values[row[2]] = values[row[0]]
#             values[row[2]] = int(row[0])
#         case 4:
#             values[row[3]] = values[row[1]] ^ 65535
#         case 5:
#             match row[1]:
#                 case 'AND':
#                     values[row[4]] = values[row[0]] & values[row[2]]
#                 case 'OR':
#                     values[row[4]] = values[row[0]] | values[row[2]]
#                 case 'LSHIFT':
#                     values[row[4]] = values[row[0]] << int(row[2])
#                 case 'RSHIFT':
#                     values[row[4]] = values[row[0]] >> int(row[2])

def findValue(x):
    # TODO: store results in {values}
    for row in text:
        row = row.split()
        if row[-1] == x:
            match len(row):
                case 3:
                    # '123' -> x
                    # 'abc' -> y
                    if row[0].islower():
                        return findValue(row[0])
                    else:
                        return int(row[0])
                case 4:
                    # NOT x -> h
                    return findValue(row[1]) ^ 65535
                case 5:
                    # x AND y -> d
                    # x OR y -> e
                    # x LSHIFT 2 -> f
                    # y RSHIFT 2 -> g
                    match row[1]:
                        case 'AND':
                            return findValue( row[0] ) & findValue( row[2] )
                        case 'OR':
                            return findValue( row[0] ) | findValue( row[2] )
                        case 'LSHIFT':
                            return findValue( row[0] ) << int(row[2])
                        case 'RSHIFT':
                            return findValue( row[0] ) >> int(row[2])
        else:
            continue

print(findValue('a'))
