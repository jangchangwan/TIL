# 2437_저울
# 2022-06-29
# 그리드

N = int(input())
N_lst = list(map(int, input().split()))

N_lst.sort()

answer = 1

for n in N_lst:
    if answer < n:
        break
    answer += n

print(answer)