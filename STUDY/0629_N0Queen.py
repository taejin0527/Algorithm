"""
 * @FileName : 0629_N0Queen.py
 * @Project : programmers
 * @Date : 2021-06-29
 * @author : AoN
 * @Link : https://programmers.co.kr/learn/courses/30/lessons/12952?language=python3
 * @Description :
 * 
"""


def possible(x, y, grid):
    for i in range(x):
        if y == grid[i] or abs(y - grid[i]) == x - i:
            return False
    return True


def queen(x, n, grid):
    if x == n:
        return 1

    count = 0

    for y in range(n):
        if possible(x, y, grid):
            grid[x] = y
            count += queen(x + 1, n, grid)

    return count


def solution(n):
    grid = [-1] * n

    answer = queen(0, n, grid)
    return answer

solution(4)