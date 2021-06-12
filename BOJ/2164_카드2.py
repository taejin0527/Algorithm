"""
@params
N           카드 개수

@return
answer      남게 되는 카드의 번호
"""

N = int(input())
cards = list(range(1, N + 1))

while len(cards) > 1:
    # 절반씩 사라짐
    cards = cards[1::2]

    if N % 2:
        cards = cards[1:] + [cards[0]]
    N //= 2
print(*cards)
