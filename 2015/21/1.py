from itertools import permutations
input = [{x[0]: int(x[1])} for x in [x.split(': ') for x in open('input.txt').read().splitlines()]]
#NOTE: [{'Hit Points': 103}, {'Damage': 9}, {'Armor': 2}]
weapons = []
armor = []
rings = []
combinations = set()
def add_item(arr, name, cost, damage, armor):
    arr.append({'name': name, 'cost': cost, 'damage': damage, 'armor': armor})

add_item(weapons, 'Dagger', 8, 4, 0)
add_item(weapons, 'Shortsword', 10, 5, 0)
add_item(weapons, 'Warhammer', 25, 6, 0)
add_item(weapons, 'Longsword', 40, 7, 0)
add_item(weapons, 'Greataxe', 74, 8, 0)

add_item(armor, 'none', 0, 0, 0)
add_item(armor, 'Leather', 13, 0, 1)
add_item(armor, 'Chainmail', 31, 0, 2)
add_item(armor, 'Splintmail', 53, 0, 3)
add_item(armor, 'Bandedmail', 75, 0, 4)
add_item(armor, 'Platemail', 102, 0, 5)

add_item(rings, 'Damage +1', 25, 1, 0)
add_item(rings, 'Damage +2', 50, 2, 0)
add_item(rings, 'Damage +3', 100, 3, 0)
add_item(rings, 'Defense +1', 20, 0, 1)
add_item(rings, 'Defense +2', 40, 0, 2)
add_item(rings, 'Defense +3', 80, 0, 3)

for weapon in weapons:
    for arm in armor:
        for k in range(3):
            for l in permutations(rings, k):
                print([weapon, arm, *l])
