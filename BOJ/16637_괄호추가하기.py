"""
@params
N           수식의 길이
expr        수식 (연산자에는 +,-,* 만 있음)

@return
answer      괄호를 적절히 추가해서 얻을 수 있는 결과의 최댓값
"""
from sys import stdin
input = stdin.readline

def divide_num_operator(expr, num, operator):
    for i in expr:
        if i.isdigit():
            num.append(int(i))
        else:
            operator.append(i)
 
 
def calc(n1, n2, operator):
    if operator == '*':
        return n1 * n2
    elif operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
 
 
def dfs(idx, ret):
    global answer
    if idx >= len(operator):
        answer = max(answer, ret)
        return
 
    # 이번에 계산 되는 경우
    dfs(idx+1, calc(ret, num[idx+1], operator[idx]))
 
    # 이번에 계산되지 않는 경우->뒤에가 먼저 계산되는 경우(괄호가 나보다 뒤에 있음)
    if idx+1 < len(operator):
        dfs(idx+2, calc(ret, calc(num[idx+1], num[idx+2], operator[idx+1]), operator[idx]))
 
 
answer = float('-inf')
N = int(input())
expr = input().rstrip()

num, operator = [], []
divide_num_operator(expr, num, operator)
dfs(0, num[0])

print(answer)