# 1817_짐 챙기는 숌
# 2022-06-11

N, M = map(int, input().split())
cnt = 0
temp = 0
if N:
    N_lst = list(map(int, input().split()))
    for n in N_lst:
        if temp + n > M:
            temp = n
            cnt += 1
        else:
            temp += n

if temp:
    print(cnt+1)
else:
    print(cnt)