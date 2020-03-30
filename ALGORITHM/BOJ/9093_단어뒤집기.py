T = int(input())
sentence = [list(map(lambda word: word[::-1], input().split())) for _ in range(T)]

for s in sentence:
    print(*s)