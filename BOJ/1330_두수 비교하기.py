A, B = map(int, input().split())
ans = ''
if A>B:
    ans = '>'
elif A<B:
    ans = '<'
else:
    ans = '=='
print(ans)