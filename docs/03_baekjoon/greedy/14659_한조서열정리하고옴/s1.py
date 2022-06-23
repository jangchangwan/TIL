# 14659_한조서열정리하고옴
# 2022-06-11

N = int(input())
N_lst = list(map(int, input().split()))


max_val = N_lst[0]
cnt = 0
max_cnt = 0
for n in range(1, N):
    if N_lst[n] >= max_val:
        max_val = N_lst[n]
        max_cnt = max(max_cnt, cnt)
        cnt = 0
    else:
        cnt += 1


max_cnt = max(max_cnt, cnt)
print(max_cnt)