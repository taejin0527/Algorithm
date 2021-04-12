stack_size = int(input())

output, stack = [], []
count = 1
valid = True

for _ in range(stack_size):
    num = int(input())

    while count <= num:
        output.append('+')
        stack.append(count)
        count += 1

    if stack[-1] == num:
        output.append('-')
        stack.pop()
    else:
        valid = False
        break

if valid:
    print(*output, sep='\n')
else:
    print('NO')

