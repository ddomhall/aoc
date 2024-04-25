text = open('input.txt').read().strip().split('\n')
text = open('test_input.txt').read().strip().split('\n')

routes = {}
for line in text:
    line = line.split()
    try:
        routes[line[0]].append([ line[2], int(line[4]) ])
    except:
        routes[line[0]] = [[ line[2], int(line[4]) ]]
    try:
        routes[line[2]].append([ line[0], int(line[4]) ])
    except:
        routes[line[2]] = [[ line[0], int(line[4]) ]]

''' {
    'London': [['Dublin', 464], ['Belfast', 518]],
    'Dublin': [['London', 464], ['Belfast', 141]],
    'Belfast': [['London', 518], ['Dublin', 141]]
} '''

