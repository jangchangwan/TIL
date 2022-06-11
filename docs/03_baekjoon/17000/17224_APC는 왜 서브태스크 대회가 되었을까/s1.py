# 17224_APC는 왜 서브태스크 대회가 되었을까?
# 2022-06-11

N, L, K = map(int, input().split())

easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

ans = min(hard, K) * 140
if hard < K:
    ans += min(K-hard, easy) * 100

print(ans)