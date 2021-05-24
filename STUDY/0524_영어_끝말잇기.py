"""
@params
n           사람의 수
words       순서대로 말한 단어

@return
answer      가장 먼저 탈락하는 사람의 번호, 그 사람이 자신의 몇 번째 차례에 탈락하는지
"""

def solution(n, words):
    answer = []
    used = set()
    
    pre = ''
    for idx, word in enumerate(words):
        if len(word) == 1:
            answer = [idx%n + 1, idx//n + 1]
            break
        
        if word in used:
            answer = [idx%n + 1, idx//n + 1]
            break
        
        if idx > 0 and pre != word[0]:
            answer = [idx%n + 1, idx//n + 1]
            break
        
        pre = word[-1]
        used.add(word)
    
    return answer if len(answer) > 0 else [0, 0]


n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
solution(n, words)