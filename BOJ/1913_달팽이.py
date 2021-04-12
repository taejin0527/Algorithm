snail_size = int(input())
search = int(input())

snail = [[0] * snail_size for _ in range(snail_size)]
next_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

num, d = snail_size ** 2, 0
current_x, current_y = 0, 0
search_x, search_y = 0, 0

while num:
    if num == search:
        search_x, search_y = current_x+1, current_y+1

    snail[current_x][current_y] = num

    next_x, next_y = current_x + next_dir[d][0], current_y + next_dir[d][1]

    if not (0 <= next_x < snail_size and 0 <= next_y < snail_size) or snail[next_x][next_y] != 0:
        d = (d + 1) % 4

    current_x, current_y  = current_x + next_dir[d][0], current_y + next_dir[d][1]
    num -= 1

for row in snail:
    print(*row)
print(search_x, search_y)
