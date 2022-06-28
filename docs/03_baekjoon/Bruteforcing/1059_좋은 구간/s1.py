# 1059 좋은 구간
# 2022-06-28
# 브루트포스
L = int(input())
S = [0] + list(map(int, input().split()))
n = int(input())

S.sort()
ans = 0
for i in range(L):
    if S[i] == n or S[i+1] == n:
        ans = 0
        break
    elif (S[i] < n) and (S[i+1] > n):
        ans = (n - S[i]) * (S[i+1] - n) - 1
        break
print(ans)