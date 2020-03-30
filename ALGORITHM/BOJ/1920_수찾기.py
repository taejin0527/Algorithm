def binary_search(left, right, key):
    mid = (left + right) // 2

    if left > right:
        return 0

    if nums[mid] == key:
        return 1
    elif nums[mid] < key:
        return binary_search(mid+1, right, key)
    else:
        return binary_search(left, mid - 1, key)


N = int(input())
nums = [int(n) for n in input().split()]
M = int(input())
comp_nums = [int(n) for n in input().split()]
nums.sort()

for n in comp_nums:
    print(binary_search(0, N-1, n))

"""
단순히 아래처럼 in 오퍼레이터를 사용하면 시간초과 뜬다
for n in comp_nums:
    print(1 if n in nums else 0)
    
in 연산자의 시간복잡도는 O(n)이라고 한다
이진탐색으로 O(log n) 시간으로 단축
"""