# https://programmers.co.kr/learn/courses/30/lessons/17681

"""
@params
n           지도의 한 변 크기
arr1        비밀지도 1 (정수 배열)
arr2        비밀지도 2 (정수 배열)

@return
answer      원래의 비밀지도 ('#', 공백)
"""

def solution(n, arr1, arr2):
    answer = []
    
    for map1, map2 in zip(arr1, arr2):
        # 2진수로 변환
        bi_map1 = bin(map1)[2:].zfill(n)
        bi_map2 = bin(map2)[2:].zfill(n)
        # answer에 담을 row
        row = ""
        
        for b1, b2 in zip(bi_map1, bi_map2):
            if b1 == '0' and b2 == '0':
                row += ' '
            else:
                row += '#'
        
        answer.append(row)

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n, arr1, arr2)
# result 	["#####","# # #", "### #", "# ##", "#####"]