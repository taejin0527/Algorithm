dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
dir_dict = {'^': 0, 'v': 1, '<': 2, '>': 3}
reversed_dict = {0: '^', 1: 'v', 2: '<', 3: '>'}
cmd_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4}


# 이 프로토 타입에서 등장하는 전차는 사용자의 전차 하나뿐이기 때문에 바로 리턴
def find_tank_pos():
    for i in range(H):
        for j in range(W):
            if mymap[i][j] in ('^', 'v', '<', '>'):
                return [i, j, mymap[i][j]]


def shoot():
    bx, by = tank_pos[0], tank_pos[1]
    b_dir = dir_dict[tank_pos[2]]
    while True:
        bx, by = bx + dx[b_dir], by + dy[b_dir]
        if 0 > bx or bx >= H or 0 > by or by >= W or mymap[bx][by] == '#':
            return
        if mymap[bx][by] == '*':
            mymap[bx][by] = '.'
            return


def move_tank(t_dir):
    cx, cy = tank_pos[0], tank_pos[1]
    nx, ny = cx + dx[t_dir], cy + dy[t_dir]

    if 0 > nx or nx >= H or 0 > ny or ny >= W or mymap[nx][ny] != '.':
        # 이동과 상관없이 탱크 방향은 바꿔준다
        mymap[cx][cy] = reversed_dict[t_dir]
        return [cx, cy, reversed_dict[t_dir]]

    # 이동할 수 있다면 현재 위치를 평지로, 이동한 위치에 탱크를 표시
    mymap[nx][ny] = reversed_dict[t_dir]
    mymap[cx][cy] = '.'
    return [nx, ny, reversed_dict[t_dir]]


for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    mymap = [list(input()) for _ in range(H)]
    input()
    cmds = input()

    tank_pos = find_tank_pos()
    for cmd in cmds:
        if cmd == 'S':
            shoot()
        else:
            tank_pos = move_tank(cmd_dict[cmd])

    print('#{} '.format(tc), end='')
    for m in mymap:
        print(''.join(m))


