N, K = [int(n) for n in input().split()]
josephus_queue = [n for n in range(1, N+1)]

order, ans = 0, []
while josephus_queue:
    order = (order + K - 1) % len(josephus_queue)
    ans.append(josephus_queue.pop(order))

print('<' + ', '.join(map(str, ans)) + '>')