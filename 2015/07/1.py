text = open('input.txt').read().strip().split('\n')
# text = '''
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i'''.strip().split('\n')

values = {}

def findValue(x):
    if x.isnumeric():
        return int(x)
    try:
        return values[x]
    except:
        for row in text:
            row = row.split()
            if row[-1] == x:
                match len(row):
                    case 3:
                        # '123' -> x
                        # 'abc' -> y
                        if row[0].islower():
                            values[x] = findValue(row[0])
                        else:
                            return int(row[0])
                    case 4:
                        # NOT x -> h
                        values[x] = int(findValue(row[1])) ^ 65535
                    case 5:
                        # x AND y -> d
                        # x OR y -> e
                        # x LSHIFT 2 -> f
                        # y RSHIFT 2 -> g
                        match row[1]:
                            case 'AND':
                                values[x] = findValue( row[0] ) & findValue( row[2] )
                            case 'OR':
                                values[x] = findValue( row[0] ) | findValue( row[2] )
                            case 'LSHIFT':
                                values[x] = findValue( row[0] ) << int(row[2])
                            case 'RSHIFT':
                                values[x] = findValue( row[0] ) >> int(row[2])
                return values[x]

print(findValue('a'))
