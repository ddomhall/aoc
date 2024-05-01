input = [{ 'number': int(x[1].rstrip(':')), x[2].rstrip(':'): int(x[3].rstrip(',')), x[4].rstrip(':'): int(x[5].rstrip(',')), x[6].rstrip(':'): int(x[7].rstrip(',')) } for x in [x.split() for x in open('input.txt').read().splitlines()]]

ref = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for sue in input:
    count = 0
    for prop in sue:
        if prop == 'number': continue
        if sue[prop] == ref[prop]: count += 1
    if count == 3: print(sue)
