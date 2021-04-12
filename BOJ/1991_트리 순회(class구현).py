def preOrder(node):
    global p_pre

    p_pre += node.data
    if node.lchild != '.':
        preOrder(binary_tree[node.lchild])
    if node.rchild != '.':
        preOrder(binary_tree[node.rchild])


def inOrder(node):
    global p_in

    if node.lchild != '.':
        inOrder(binary_tree[node.lchild])
    p_in += node.data
    if node.rchild != '.':
        inOrder(binary_tree[node.rchild])


def postOrder(node):
    global p_post

    if node.lchild != '.':
        postOrder(binary_tree[node.lchild])
    if node.rchild != '.':
        postOrder(binary_tree[node.rchild])
    p_post += node.data


class Node:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


N = int(input())
binary_tree = {}
for _ in range(N):
    root, left, right = input().split()
    binary_tree[root] = Node(root, left, right)

tree_root = binary_tree['A']
p_pre, p_in, p_post = '', '', ''

preOrder(tree_root)
print(p_pre)
inOrder(tree_root)
print(p_in)
postOrder(tree_root)
print(p_post)