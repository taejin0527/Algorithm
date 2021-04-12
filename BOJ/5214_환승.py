import sys
input = sys.stdin.readline

def bfs():
    visit[1] = 1
    qu =[1]
    while qu:
        x = qu.pop(0)
        if x==N:return visit[x]
        for n in dp[x]:
            if not visit[n]:
                if n>N:visit[n] = visit[x]
                else: visit[n] = visit[x]+1
                qu.append(n)
    return -1

N,K,M =map(int,input().split())
dp = [[] for _ in range(N+M+1)]
for i in range(1,M+1):
    nums = [*map(int,input().split())]
    for n in nums:
        dp[N+i].append(n)
        dp[n].append(N+i)
visit = [0]*(N+M+1)
print(bfs())