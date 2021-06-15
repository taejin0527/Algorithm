"""
@params
* 여러 테스트케이스 존재 (0 0 입력되면 종료)
n, m                    정점의 개수, 간선의 개수
[u, v] * m              간선 정보

@return
그래프에 트리가 없다면 "No trees."를, 
한 개라면 "There is one tree."를, 
T개(T > 1)라면 "A forest of T trees."
"""
from sys import stdin
input = stdin.readline

def is_tree(prev: int, cur: int) -> bool:
    visited[cur] = True

    for nxt_node in graph[cur]:
        if nxt_node == prev:
            continue
        if visited[nxt_node]:
            return False
        
        if not is_tree(cur, nxt_node):
            return False

    return True

print_buf = []
case_no = 0
while True:
    case_no += 1
    n, m = map(int, input().split())

    if (n, m) == (0, 0):
        break

    graph = [[] for _ in range(n+1)]        # adj graph
    visited = [False] * (n+1)               # check visited node

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    tree_cnt = 0
    for node in range(1, n+1):
        if not visited[node]:
            if is_tree(0, node):
                tree_cnt += 1

    if tree_cnt > 1:
        print_buf.append(f"Case {case_no}: A forest of {tree_cnt} trees.")
    elif tree_cnt == 1:
        print_buf.append(f"Case {case_no}: There is one tree.")
    else:
        print_buf.append(f"Case {case_no}: No trees.")

print("\n".join(print_buf))