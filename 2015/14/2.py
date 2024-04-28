input = [{ 'name': x[0], 'speed': int(x[3]), 'time': int(x[6]), 'rest': int(x[13]), 'distance': 0, 'points': 0 } for x in [x.split() for x in open('input.txt').read().splitlines()]]

lead = winner = input[0]
for second in range(2503):
    for deer in input:
        if second % (deer['time'] + deer['rest']) < deer['time']:
            deer['distance'] += deer['speed']
        if deer['distance'] > lead['distance']: lead = deer
    for deer in input:
        if deer['distance'] == lead['distance']:
            deer['points'] += 1
        if deer['points'] > winner['points']: winner = deer

print(winner)

