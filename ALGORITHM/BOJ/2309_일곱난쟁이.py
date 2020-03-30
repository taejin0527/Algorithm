from itertools import combinations

dwarf = sorted([int(input()) for _ in range(9)])

for seven_dwarf in combinations(dwarf, 7):
    if sum(seven_dwarf) == 100:
        print(*seven_dwarf, sep='\n')
        break
