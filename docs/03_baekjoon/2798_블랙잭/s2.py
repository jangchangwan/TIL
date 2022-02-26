import sys
sys.stdin = open("input.txt", 'r')

N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
max_sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            now_sum = N_lst[i] + N_lst[j] + N_lst[k]
            if max_sum < now_sum <= M:
                max_sum = now_sum
print(max_sum)