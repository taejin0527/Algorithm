def rotate(f):
    # 윗면을 초기값으로 겨냥도를 상상한다
    sketch = cube['U'], cube['L'], cube['F'], cube['R'], cube['B']

    # 회전시킬 면에 따라 겨냥도를 수정한다(주의, 모든 면이 순환하는 형태)
    if f == 'L':
        sketch = cube['L'], cube['F'], cube['U'], cube['B'], cube['D']
    if f == 'F':
        sketch = cube['F'], cube['U'], cube['L'], cube['D'], cube['R']
    if f == 'R':
        sketch = cube['R'], cube['D'], cube['B'], cube['U'], cube['F']
    if f == 'B':
        sketch = cube['B'], cube['R'], cube['D'], cube['L'], cube['U']
    if f == 'D':
        sketch = cube['D'], cube['B'], cube['R'], cube['F'], cube['L']

    # 수정된 겨냥도의 정면, 위, 오른쪽, 아래, 왼쪽
    U, L, F, R, B = sketch

    # 정면을 회전시킨다 (정가운데는 변화가 없다)
    U[0][2], U[1][2], U[2][2], U[2][1], U[2][0], U[1][0], U[0][0], U[0][1] =\
        U[0][0], U[0][1], U[0][2], U[1][2], U[2][2], U[2][1], U[2][0], U[1][0]

    front = F[2][0], F[1][0], F[0][0]
    right = R[0][2], R[1][2], R[2][2]
    back = B[0][0], B[0][1], B[0][2]
    left = L[2][2], L[2][1], L[2][0]
    L[2][2], L[2][1], L[2][0] = front
    F[2][0], F[1][0], F[0][0] = right
    R[0][2], R[1][2], R[2][2] = back
    B[0][0], B[0][1], B[0][2] = left


for test_case in range(int(input())):
    n = int(input())
    r = list(input().split())
    cube = {
        'U': [['w'] * 3 for _ in range(3)],
        'D': [['y'] * 3 for _ in range(3)],
        'F': [['r'] * 3 for _ in range(3)],
        'B': [['o'] * 3 for _ in range(3)],
        'L': [['g'] * 3 for _ in range(3)],
        'R': [['b'] * 3 for _ in range(3)],
    }

    for face, _dir in r:
        if _dir == '+':
            rotate(face)
        elif _dir == '-':
            rotate(face)
            rotate(face)
            rotate(face)

    for i in range(3):
        print("".join(color for color in cube['U'][i]))
