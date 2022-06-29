# 1715_카드 정렬하기
# 2022-06-29
# 우선순위 큐

import heapq

N = int(input())
N_lst = [int(input()) for _ in range(N)]
heapq.heapify(N_lst)


ans = 0
while len(N_lst) != 1:
    sum_N = heapq.heappop(N_lst) + heapq.heappop(N_lst)
    ans += sum_N
    heapq.heappush(N_lst, sum_N)

print(ans)