razor = input()

razor_len = len(razor)
stack, count = [], 0

for i in range(razor_len):
    if razor[i] == '(':
        stack.append('(')

    else:
        if razor[i - 1] == '(':
            stack.pop()
            count += len(stack)

        else:
            stack.pop()
            count += 1

print(count)