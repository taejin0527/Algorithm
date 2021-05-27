# https://www.acmicpc.net/problem/14725

"""
@params
N               로봇 개미가 각 층을 따라 내려오면서 알게 된 먹이의 정보 개수
K, *args        로봇 개미 한마리가 보내준 먹이 정보 개수, 각 층마다 지나온 방에 있는 먹이 정보(길이 t)

@return
answer          개미굴의 시각화된 구조
"""
from sys import stdin

input = stdin.readline

N = int(input())
antInfoList = []
for _ in range(N):
    K, *args = input().split()
    antInfoList.append(args)

antInfoList.sort()
for i in range(N):
    existRoom = False
    for j in range(len(antInfoList[i])):
        if i == 0 or existRoom:
            print("--" * j + antInfoList[i][j])

        elif antInfoList[i - 1][j] != antInfoList[i][j]:
            existRoom = True
            print("--" * j + antInfoList[i][j])
