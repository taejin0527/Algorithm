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

# 시간 초과...ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ


def status(T: int) -> str:
    if T == 0:
        return "No trees."
    elif T == 1:
        return "There is one tree."
    elif T > 1:
        return f"A forest of {T} trees."


class Disjoint_set:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size + 1))
        self.cycle_group = set()

    def find(self, a: int) -> int:
        if self.parent[a] == a:
            return a
        p = self.find(self.parent[a])
        self.parent[a] = p

        return p

    def union(self, a: int, b: int) -> None:
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            self.cycle_group.add(pa)
        elif pa > pb:
            self.parent[pb] = pa
        else:
            self.parent[pa] = pb

    def count_tree(self) -> int:
        return len(set(self.find(i) for i in self.parent[1:])) - len(self.cycle_group)

    def __str__(self):
        return ",".join(map(str, self.parent))


case_no = 0
while True:
    case_no += 1

    n, m = map(int, input().split())

    if (n, m) == (0, 0):
        break

    disjoint_set = Disjoint_set(n)
    for _ in range(m):
        u, v = map(int, input().split())
        disjoint_set.union(u, v)

    num_of_tree = disjoint_set.count_tree()
    answer = f"Case {case_no}: {status(num_of_tree)}"

    print(answer)
