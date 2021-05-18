# https://programmers.co.kr/learn/courses/30/lessons/77486

class DisjointSet:
    def __init__(self, size):
        self.data = list(range(size))
        self.size = size

    def find(self, x):
        return self.data[x]


    def union(self, x, y):
        self.data[x] = y

    
    def toString(self):
        return self.data


"""
@params
enroll          각 판매원의 이름
referral        다단계 조직에 참여시킨 다른 판매원의 이름
seller          판매량 집계 데이터의 판매원 이름 (같은 이름이 중복 가능)
amount          판매량 집계 데이터의 판매 수량

@return
answer          각 판매원이 득한 이익금을 나열한 배열 (enroll에 이름이 포함된 순서에 따라 나열)
"""
def solution(enroll, referral, seller, amount):
    answer = []

    # dict형으로 순서 기억
    enroll_dict = {}
    for idx, e in enumerate(enroll):
        enroll_dict[e] = idx
        
    print(enroll_dict)
    
    # 초기화
    disjoint = DisjointSet(len(enroll))
    # union 으로 그래프 그리고
    for a, b in zip(enroll, referral):
        x = enroll_dict[a]
        y = -1 if b == '-' else enroll_dict[b]

        disjoint.union(x, y)

    print(disjoint.toString())
    
    # seller, amount 순서대로 그래프 타면서 이익금 계산
    answer = [0] * len(enroll)
    for s, a in zip(seller, amount):
        x = enroll_dict[s]
        
        answer[x] += a * 90
        
    print(answer)
    # answer에 넣기

    
    return answer



enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

solution(enroll, referral, seller, amount)
# answer [360, 958, 108, 0, 450, 18, 180, 1080]