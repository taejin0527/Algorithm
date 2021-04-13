# 핀볼 방향 { 상: 0, 하: 1, 좌: 2, 우: 3 }
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
# 방향에 따라 해당 블록에서 튕기는 방향
blocks = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2]
}


for tc in range(int(input())):
    N = int(input()) # 게임판 크기 N * N
    
    # 게임판 입력 { 블랙홀: -1, 빈 칸: 0, 블록: 1~5, 웜홀: 6~10 }
    # 5번 블록을 추가해서 벽 생성
    game_board = [[5] * (N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N+2)]
    
    # 시간 절약을 위해 웜홀 위치를 미리 파악
    wormhole = {}
    wormhole_start = {}
    for x in range(1, N+1):
        for y in range(1, N+1):
            num = game_board[x][y]
            if num in range(6, 11):                      # 6~10이면 웜홀
                if num not in wormhole_start:            # 아직 짝이 없으면 start에 넣어둠
                    wormhole_start[num] = (x, y)
                else:                                    # 앞서 해당 번호의 웜홀이 있었으면 wormhole 딕셔너리에 등록
                    wormhole[wormhole_start[num]] = (x, y)
                    wormhole[(x, y)] = wormhole_start[num]
    
    
    max_score = 0
    for x in range(1, N+1):
        for y in range(1, N+1):
            if game_board[x][y] == 0:                                               # 빈 공간이면 시작점으로 잡고
                start_point = x, y

                for d in range(4):                                                  # 4 방향으로 핀볼을 보냄
                    nx, ny = x + dir[d][0], y + dir[d][1]                               # 다음 이동 위치
                    score = 0                                                           # 현재 스코어
                    
                    while True:
                        cur = game_board[nx][ny]
                        if (nx, ny) == start_point or cur == -1:                    # 시작점이거나 블랙홀이면 
                            break                                                       # 게임 종료
                            
                        if cur in range(1, 6):                                      # 일반 블록이면                            
                            d = blocks[cur][d]                                          # 방향을 바꾸고
                            score += 1                                                  # 스코어 +1
                            
                        if cur in range(6, 11):                                     # 웜홀이면
                            nx, ny = wormhole[(nx, ny)]                                 # 워프함
                            
                        nx, ny = nx + dir[d][0], ny + dir[d][1]
                        
                    max_score = max(score, max_score)                                   # 게임 종료마다 최대값 갱신
    
    print(f'#{tc+1} {max_score}')