from collections import defaultdict

visited = defaultdict(int)
input = 36000000
elf = 1

for elf in range(1, input):
    for house in range(elf, elf*50+1, elf):
        visited[house] += elf*11
    if visited[elf] >= input:
        break

print(elf)
