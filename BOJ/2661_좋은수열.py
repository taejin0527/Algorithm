"""
 * @FileName : 2661_좋은수열.py
 * @Project : BOJ
 * @Date : 2020-12-03
 * @author : AoN
 * @Link : https://www.acmicpc.net/problem/2661
 * @Description : Backtracking
 * 
"""

N = int(input())


def dfs(i, s):
    for j in range(1, i//2+1):
        if s[i-(2*j):i-j] == s[i-j:]:
            return

    if i == N:
        print(*s, sep='')
        exit(0)

    for num in (1, 2, 3):
        if s and s[-1] == num:
            continue

        dfs(i+1, s + [num])


dfs(0, [])
