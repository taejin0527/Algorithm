from collections import deque


def bfs(p1, p2):
    visited, queue = [], deque([p1])
    cnt = -1

    while queue:
        cnt += 1
        length = len(queue)

        for _ in range(length):
            person = queue.popleft()

            if person == p2:
                return cnt

            for search in family_tree[person]:
                if search not in visited:
                    visited.append(search)
                    queue.append(search)

    return -1


num_of_people = int(input())
family_tree = {x: set() for x in range(1, num_of_people+1)}
person_1, person_2 = map(int, input().split())
edges = int(input())
for _ in range(edges):
    x, y = map(int, input().split())
    family_tree[x].add(y)
    family_tree[y].add(x)

print(bfs(person_1, person_2))



####################################################################################

# from collections import defaultdict
#
# n = int(input())
# a, b = map(int, input().split())
# t = int(input())
# d = defaultdict(set)
#
# for _ in range(t):
#     x, y = map(int, input().split())
#     d[x].add(y)
#     d[y].add(x)
#
#
# def bfs(a, b):
#     q, visited = [a], {a}
#     step = 0
#
#     while q:
#         size = len(q)
#         for i in range(size):
#             cur = q.pop(0)
#             if cur == b:
#                 return step
#
#             for j in d[cur]:
#                 if j not in visited:
#                     visited.add(j)
#                     q.append(j)
#
#         step += 1
#
#     return -1
#
#
# print(bfs(a, b))

