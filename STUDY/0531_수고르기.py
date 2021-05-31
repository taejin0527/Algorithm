"""
@params
N, M        숫자의 개수, 차이
[list]      수열

@return
answer      M 이상이면서 가장 작은 차이

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = [int(input()) for _ in range(N)]

sequence.sort()

def find_M():
    left, right = 0, 1
    answer = sys.maxsize

    while left < N and right < N:
        diff = sequence[right] - sequence[left]

        if diff == M:
            return M

        if diff < M:
            right += 1
            continue
        left += 1
        answer = min(answer, diff)

    return answer

print(find_M())