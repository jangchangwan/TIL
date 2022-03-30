# 1764_듣보잡_문제풀이
# 2022-03-30
# 시간초과
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

N_lst = [input() for _ in range(N)]
M_lst = [input() for _ in range(M)]


cnt = 0
ans_lst = []
for n in range(N):
    for m in range(M):
        if N_lst[n] == M_lst[m]:
            cnt += 1
            ans_lst.append(N_lst[n])

print(cnt)
ans_lst.sort()
for ans in ans_lst:
    print(ans)