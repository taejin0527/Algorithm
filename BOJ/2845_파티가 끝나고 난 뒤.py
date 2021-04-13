L, P = map(int, input().split())
news = list(map(int, input().split()))
print(*list(map(lambda n: n - L*P, news)))