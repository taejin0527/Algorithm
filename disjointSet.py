from collections import deque
from sys import stdin
from typing import Counter
input = stdin.readline

class DisjointSet:
    def __init__(self, size) -> None:
        self.parent = [-1] * size
        self.depth = size
        
    def find(self, idx) -> int:
        value = self.parent[idx]
        
        if value < 0:
            return idx
        
        return self.find(value)

    def union(self, a, b) -> None:
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return
        
        if self.parent[a] > self.parent[b]:
            self.parent[a] = b
        elif self.parent[a] < self.parent[b]:
            self.parent[b] = a
        else:
            self.parent[a] -= 1
            self.parent[b] = a
            
        self.depth -= 1
            
    def toString(self) -> list:
        return self.parent
    def size(self) -> int:
        return self.depth
"""
@params
N, M            사람의 수, 친구 관계의 수
[list]          a와 b가 친구

@return
answer          조건에 맞는 A, B, C, D, E가 존재하면 1, 없으면 0
"""

N, M = map(int, input().split())
friends = DisjointSet(N)

for _ in range(M):
    a, b = map(int, input().split())
    friends.union(a, b)
    
print(friends.toString())
tmp = filter(lambda x: x>=0, friends.toString())
tmp.sort()

cnt = 0
flag = False
for i in range(len(tmp)-1):
    if tmp[i] == tmp[i+1]:
       cnt += 1
       if cnt >= 4:
           flag = True
           break
    else:
        cnt = 0
        
    
print(1 if flag else 0)