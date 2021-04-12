def eratosthenes():
    sieve = [True] * 1001   # 1,000 이하의 자연수만 입력됨
    sieve[0] = sieve[1] = False

    for idx, prime in enumerate(sieve):
        if prime:
            for jump in range(idx*idx, 1001, idx):
                sieve[jump] = False
    return sieve


primes = eratosthenes() # 1,000 이하의 자연수 중 소수들을 리스트에 저장

N = input()
numbers = map(int, input().split())

count = 0
for i in numbers:
    if primes[i]:
        count += 1
print(count)
