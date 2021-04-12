def eratosthenes():
    sieve = [True] * 1000001
    sieve[0] = sieve[1] = False

    for idx, prime in enumerate(sieve):
        if prime:
            for jump in range(idx * idx, 1000001, idx):
                sieve[jump] = False
    return sieve


primes = eratosthenes()  # 1,000,000 이하의 자연수 중 소수들을 리스트에 저장

while True:
    even_number = int(input())
    if not even_number:
        break

    for i in range(2, 1000001):
        x, y = i, even_number - i
        if primes[x] and primes[y] and (x + y == even_number):
            print(f'{even_number} = {x} + {y}')
            break
