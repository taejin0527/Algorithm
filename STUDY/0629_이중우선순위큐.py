"""
 * @FileName : 0629_이중우선순위큐.py
 * @Project : programmers
 * @Date : 2021-06-29
 * @author : AoN
 * @Link : https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
 * @Description :
 * 
"""
import heapq


def changeHeap(hq):
    q = []
    for n in hq:
        heapq.heappush(q, -n)
    return q


def solution(operations):
    answer = []  # [최댓값, 최솟값]
    minheap = []
    maxheap = []

    for o in operations:
        command, num = o.split(' ')
        num = int(num)
        if command == 'I':
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
        elif command == 'D':
            try:
                if num == 1:
                    heapq.heappop(maxheap)
                    minheap = changeHeap(maxheap)
                else:
                    heapq.heappop(minheap)
                    maxheap = changeHeap(minheap)
            except:
                continue

    if len(maxheap) != 0:
        answer.append(-maxheap[0])
    else:
        answer.append(0)
    if len(minheap) != 0:
        answer.append(minheap[0])
    else:
        answer.append(0)
    return answer



op = ["I 7","I 5","I -5","D -1"]
a = solution(op)
print(a)