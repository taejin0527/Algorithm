"""
Trie(트라이) 자료구조
- 문자열에 특화된 자료구조
"""
class Node:
    def __init__(self) -> None:
        self.child = {}
        self.isTail = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def add(self, foods: list) -> None:
        node = self.root

        for food in foods:
            if food not in node.child:
                node.child[food] = Node()
            node = node.child[food]
        node.isTail = True

    def travel(self, level: int, node: Node) -> None:
        if node.isTail:
            return

        sorted_node = sorted(node.child)

        for child in sorted_node:
            print("--" * level + child)
            self.travel(level + 1, node.child[child])


N = int(input())
antHill = Trie()

for _ in range(N):
    K, *args = input().split()
    antHill.add(args)

antHill.travel(0, antHill.root)
