piece = (1, 1, 2, 2, 2, 8)
white = map(int, input().split())
res = []
for a, b in zip(piece, white):
    res.append(a - b)
    
print(*res)