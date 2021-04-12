"""
 * @FileName : 9663_nQeen.py
 * @Project : BOJ
 * @Date : 2020-12-02
 * @author : AoN
 * @Link : https://www.acmicpc.net/problem/9663
 * @Description :
 * 
"""

N, ans = int(input()), 0
a, b, c = [False] * N, [False] * (2*N-1), [False] * (2*N-1)


def dfs(x):
    global ans

    if x == N:
        ans += 1
        return

    for y in range(N):
        if not (a[y] or b[x+y] or c[x-y+N-1]):
            a[y] = b[x+y] = c[x-y+N-1] = True
            dfs(x+1)
            a[y] = b[x + y] = c[x - y + N - 1] = False


dfs(0)
print(ans)

