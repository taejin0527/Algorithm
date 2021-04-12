num_of_factors = int(input())
factors = [int(num) for num in input().split()]
factors.sort()

min_factor, max_factor = factors[0], factors[-1]
print(min_factor * max_factor)