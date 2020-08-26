def solution(n, arr1, arr2):
    answer = []

    for num1, num2 in zip(arr1, arr2):
        # or 비트 연산으로 두 배열을 합치고(불필요한 0b 문자를 떼기 위해 [2:]부터 시작)
        num12 = str(bin(num1 | num2))[2:]
        # 앞의 공백을 채워주기 위해 zfil() 사용, rjust()를 사용해도 무방
        num12 = num12.zfill(n)
        # 2진수를 매칭되는 기호로 변환
        num12 = num12.replace('0', ' ')
        num12 = num12.replace('1', '#')
        # 정답 배열에 추가
        answer.append(num12)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))


"""
다른 분들의 코드
https://programmers.co.kr/learn/courses/30/lessons/17681/solution_groups?language=python3

<인상 깊은 한 줄 코딩>
solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])
"""