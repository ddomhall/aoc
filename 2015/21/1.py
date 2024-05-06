from itertools import permutations
from copy import deepcopy
from sys import maxsize

input = open('input.txt').read().split()
input = {'hp': int(input[2]), 'damage': int(input[4]), 'armor': int(input[6])}
combinations = []
weapons_list = []
armor_list = []
rings_list = []
best = maxsize

def add_item(arr, name, cost, damage, armor):
    arr.append({'name': name, 'cost': cost, 'damage': damage, 'armor': armor})

add_item(weapons_list, 'Dagger', 8, 4, 0)
add_item(weapons_list, 'Shortsword', 10, 5, 0)
add_item(weapons_list, 'Warhammer', 25, 6, 0)
add_item(weapons_list, 'Longsword', 40, 7, 0)
add_item(weapons_list, 'Greataxe', 74, 8, 0)

add_item(armor_list, 'none', 0, 0, 0)
add_item(armor_list, 'Leather', 13, 0, 1)
add_item(armor_list, 'Chainmail', 31, 0, 2)
add_item(armor_list, 'Splintmail', 53, 0, 3)
add_item(armor_list, 'Bandedmail', 75, 0, 4)
add_item(armor_list, 'Platemail', 102, 0, 5)

add_item(rings_list, 'Damage +1', 25, 1, 0)
add_item(rings_list, 'Damage +2', 50, 2, 0)
add_item(rings_list, 'Damage +3', 100, 3, 0)
add_item(rings_list, 'Defense +1', 20, 0, 1)
add_item(rings_list, 'Defense +2', 40, 0, 2)
add_item(rings_list, 'Defense +3', 80, 0, 3)

for weapon in weapons_list:
    for arm in armor_list:
        for quantity in range(3):
            for rings in permutations(rings_list, quantity):
                combinations.append([weapon, arm, *rings])

for combination in combinations:
    cost = sum(item['cost'] for item in combination)
    player = {'hp': 100, 'damage' : sum(item['damage'] for item in combination), 'armor' : sum(item['armor'] for item in combination) }
    boss = deepcopy(input)
    winner = False
    player_turn = True

    while not winner:
        if player_turn:
            diff = player['damage'] - boss['armor']
            if diff > 0:
                boss['hp'] -= diff
            else:
                boss['hp'] -= 1
        else:
            diff = boss['damage'] - player['armor']
            if diff > 0:
                player['hp'] -= diff
            else:
                player['hp'] -= 1

        if player['hp'] <= 0:
            winner = boss
        elif boss['hp'] <= 0:
            winner = player
        else:
            player_turn = not player_turn

    if winner == player:
        if cost < best: best = cost

print(best)
