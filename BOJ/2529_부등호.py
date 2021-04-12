K = int(input())
signs = input().split()
v = [False] * 10
mx, mn = "", ""


def check(a, b, op):
    if op == '<':
        return a < b
    if op == '>':
        return a > b
    return False


def dfs(depth, seq):
    global mx, mn
    if depth == K+1:
        if not len(mn):
            mn = seq
        else:
            mx = seq
        return

    for i in range(10):
        if not v[i] and (depth == 0 or check(seq[-1], str(i), signs[depth-1])):
            v[i] = True
            dfs(depth+1, seq + str(i))
            v[i] = False


dfs(0, "")
print(mx, mn, sep='\n')