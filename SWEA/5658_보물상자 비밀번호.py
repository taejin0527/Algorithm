for tc in range(int(input())):
    ans = 0
    N, K = map(int, input().split())
    singleLine = N // 4                 # 자물쇠 한 줄에 있는 번호 개수
    combSet = set()                     # 가능한 숫자 집합

    numArr = list(input())

    for k in range(singleLine):         # 한 줄에 있는 번호 개수만큼 회전하면 뒤에는 이전과 동일하다
        for i in range(4):
            num = ''
            for j in range(singleLine):
                num += numArr[i*singleLine + j]
            num = int(num, 16)

            if num not in combSet:
                combSet.add(num)
        numArr = numArr[1:] + numArr[:1]

    combSet = sorted(list(combSet), reverse=True)

    ans = combSet[K-1]

    print("#{} {}".format(tc+1, ans))
