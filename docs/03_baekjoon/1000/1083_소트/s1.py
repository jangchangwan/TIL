# 1083_소트_문제풀이
# 2022-06-07

N = int(input())

N_lst = list(map(int, input().split()))
S = int(input())

for i in range(N-1):
    max_num = N_lst[i]
    val = 0
    if S == 0:
        break
    for j in range(i+1, N):
        x = j - i
        if N_lst[j] > max_num:
            max_num = N_lst[j]
            val = x
        if x >= S:
            break

    if val:
        S -= val
        N_lst.remove(max_num)
        N_lst.insert(i, max_num)

print(*N_lst)
