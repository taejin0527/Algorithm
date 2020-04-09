def before_permutation(a):
    length = len(a) - 1

    i = length
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i == 0:
        return False

    j = length
    while a[i-1] <= a[j]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = length
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


N = input()
A = list(map(int, input().split()))

if before_permutation(A):
    print(*A)
else:
    print(-1)