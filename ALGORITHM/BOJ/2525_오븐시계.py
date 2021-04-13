A, B = map(int, input().split())
C = int(input())

B += C
if B >= 60:
    a = B // 60
    A = (A + a) % 24
    B = B % 60

print(A, B)