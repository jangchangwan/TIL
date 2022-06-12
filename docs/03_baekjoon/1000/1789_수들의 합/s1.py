# 1789_수들의합
# 2022-06-11

S = int(input())

total = 0
i = 0

while total <= S:
    i += 1
    total += i

print(i-1)
