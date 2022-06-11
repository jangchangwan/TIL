# 21313_문어
# 2022-06-11

N = int(input())
ans = [1, 2] * (N//2)
if N % 2:
    ans += [3]
print(*ans)