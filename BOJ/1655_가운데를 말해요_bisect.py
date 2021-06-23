"""
시간초과....ㅠㅠ
"""

from bisect import bisect_left
from sys import stdin

input = stdin.readline

n = int(input())  # 수빈이가 외치는 정수의 개수 입력받기
array = []  # 입력받은 숫자를 저장할 리스트 선언
print_buf = []

# 첫 번째 숫자 입력받기
num = int(input())
array.append(num)
print_buf.append(num)

# array 현재 길이
length = 1

# 두 번째 숫자부터 차례대로 입력받기
for _ in range(n - 1):
    num = int(input())
    # 숫자가 삽입 될 인덱스 찾기
    index = bisect_left(array, num)
    # 숫자 삽입, array 길이 1 증가
    array.insert(index, num)
    length += 1

    if length % 2 == 0:  # 짝수개
        print_buf.append(array[length // 2 - 1])
    else:
        print_buf.append(array[length // 2])

print(*print_buf, sep="\n")
