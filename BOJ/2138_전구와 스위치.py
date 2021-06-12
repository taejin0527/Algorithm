"""
@params
N                   전구의 개수
[asIs]              전구들의 현재 상태
[toBe]              만들고자 하는 전구들의 상태

@return
answer              상태를 만들기 위해 스위치를 눌러야하는 최소 횟수(불가능: -1)
"""

N = int(input())
asIs = list(map(int, input()))
toBe = list(map(int, input()))


def switch(status):
    return 0 if status == 1 else 1


def greedy(asIs, cnt):
    if cnt == 1:
        asIs[0] = switch(asIs[0])
        asIs[1] = switch(asIs[1])

    for i in range(1, N):
        if asIs[i-1] != toBe[i-1]:
            cnt += 1
            asIs[i-1] = switch(asIs[i-1])
            asIs[i] = switch(asIs[i])
            if i == N-1:
                continue
            asIs[i+1] = switch(asIs[i+1])

    if asIs == toBe:
        return cnt
    else:
        return -1

res1 = greedy(asIs[:], 0)
res2 = greedy(asIs[:], 1)

if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1>=0 and res2 < 0:
    print(res1)
elif res1 <0 and res2 >= 0:
    print(res2)
else:
    print(-1)
