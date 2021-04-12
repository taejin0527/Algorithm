def next_permutation(a):
    reset_len = len(a) - 1

    i = reset_len
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i == 0:
        return False

    j = reset_len
    while a[i - 1] >= a[j]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]  # SWAP

    j = reset_len
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


N = input()
A = list(map(int, input().split()))

if next_permutation(A):
    print(*A)
else:
    print(-1)
