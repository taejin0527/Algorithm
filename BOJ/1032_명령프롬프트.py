"""
PATTERN: alphabet, ".", "?"
"""

num_of_files = int(input())
file_names = [input() for _ in range(num_of_files)]

pattern = ""

for c in zip(*file_names):
    if len(set(c)) == 1:
        pattern += c[0]
    else:
        pattern += '?'

print(pattern)

# zip() 함수 사용과 집합 set()을 사용하는 매우 기발한 아이디어
