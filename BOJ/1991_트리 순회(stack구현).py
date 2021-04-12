from collections import defaultdict


def preOrder(start):
    stack = [start]
    result = ''

    while stack:
        node = stack.pop()
        result += node

        if binary_tree[node][1] != '.':
            stack.append(binary_tree[node][1])

        if binary_tree[node][0] != '.':
            stack.append(binary_tree[node][0])

    return result


def inOrder(start):
    stack = [start]
    result = ''

    while stack:
        if binary_tree[stack[-1]][0] != '.' and binary_tree[stack[-1]][0] not in result:
            stack.append(binary_tree[stack[-1]][0])

        elif stack[-1] in result:
            stack.append(binary_tree[stack[-1]][1])

        else:
            node = stack.pop()
            result += node
            if binary_tree[node][1] != '.':
                stack.append(binary_tree[node][1])

    return result


def postOrder(start):
    stack = [start]
    result = ''

    while stack:
        if binary_tree[stack[-1]][0] != '.' and binary_tree[stack[-1]][0] not in result:
            stack.append(binary_tree[stack[-1]][0])

        elif binary_tree[stack[-1]][1] == '.' or binary_tree[stack[-1]][1] in result:
            result += stack.pop()

        else:
            stack.append(binary_tree[stack[-1]][1])

    return result


N = int(input())
binary_tree = defaultdict(list)
for _ in range(N):
    root, left, right = input().split()
    binary_tree[root] = [left, right]

tree_root = 'A'
print(preOrder(tree_root))
print(inOrder(tree_root))
print(postOrder(tree_root))