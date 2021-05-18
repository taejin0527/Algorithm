# https://programmers.co.kr/learn/courses/30/lessons/60059

"""
@params
key         array(열쇠) M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열
lock        array(자물쇠) N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열

@return
result      true/false
"""
def solution(key, lock):
    cnt = 0
    
    for row in lock:
        cnt += row.count(0)
        
    if cnt == 0:
        return True
    
    # 지도를 확장
    M, N = len(key), len(lock)
    MN = 2 * M + N - 2
    map = [[0] * MN for _ in range(MN)]
    
    for x in range(N):
        for y in range(N):
            map[x + M - 1][y + M - 1] = lock[x][y]
    
    # print(*map, sep='\n')

    for x in range(N + M - 1):
        for y in range(N + M - 1):
            
            for _ in range(4):
                # 회전
                key = list(zip(*key))[::-1]
                # key 복사
                copy_map = [row[:] for row in map]
                check = False
                
                for r in range(M):
                    for c in range(M):    
                        #  열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다 (주의!!!)
                        if copy_map[r+x][c+y] == 1 and key[r][c] == 1:
                            check = True
                            break
                        
                        if copy_map[r+x][c+y] == 0:
                            copy_map[r + x][c + y] = key[r][c]
                    if check:
                        break
                
                # print(*copy_map, sep="\n")
                # print("=================================")

                # 확인
                for r in range(M-1, M + N - 1):
                    for c in range(M-1, M + N - 1):
                        if copy_map[r][c] == 0:
                            check = True
                            break
                    
                    if check:
                        break
                        
                if not check:
                    return True

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key, lock)