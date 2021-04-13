A, B, C = map(int, input().split())
D = int(input())

C += D
sec = C % 60
B += C//60
min = B % 60
A += B//60
hour = A % 24

print(hour, min, sec)