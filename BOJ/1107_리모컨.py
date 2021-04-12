"""
 * @FileName : 1107_리모컨.py
 * @Project : LeetCode
 * @Date : 2021-02-01
 * @author : AoN
 * @Link :
 * @Description :
 * 
"""
import sys
input = sys.stdin.readline

def check(num):
    num = list(str(num))
    for i in num:
        if i in buttons: return False
    return True


N = int(input())
M = int(input())
buttons = list(input().strip())

ans = abs(N - 100)
for i in range(1000001):
    if check(i):
        ans = min(ans, len(str(i)) + abs(N-i))

print(ans)