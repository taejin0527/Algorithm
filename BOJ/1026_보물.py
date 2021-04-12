N = int(input())
array_A = [int(n) for n in input().split()]
array_B = [int(n) for n in input().split()]

product_sum = list(map(lambda a, b: a*b, sorted(array_A), sorted(array_B, reverse=True)))
print(sum(product_sum))