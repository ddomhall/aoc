text = open('input.txt').read().strip().split('\n')

routes = []
for line in text:
    line = line.split()
    routes.append({'route': [line[0], line[2]], 'distance': line[4] })

