input = [{ 'name': x[0], 'speed': int(x[3]), 'time': int(x[6]), 'rest': int(x[13]) } for x in [x.split() for x in open('input.txt').read().splitlines()]]

topDistance = 0
for deer in input:
    times = divmod(2503, (deer['time'] + deer['rest']))
    distance = times[0] * deer['speed'] * deer['time']
    if times[1] > deer['time']:
        distance += deer['speed'] * deer['time']
    else:
        distance += deer['speed'] * times[1]
    if distance > topDistance: topDistance = distance

print(topDistance)
