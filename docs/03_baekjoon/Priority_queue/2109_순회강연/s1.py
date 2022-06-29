# 2109_순회강연
# 2022-06-29
# 우선순위 큐 + 그리드

import heapq

N = int(input())
N_lst = [list(map(int, input().split())) for _ in range(N)]

# D-Day로 정렬한다
N_lst.sort(key=lambda x: x[1])

answer = []
for n in N_lst:
    # 강연비를 넣는다
    heapq.heappush(answer, n[0])
    # D-day 비교
    if len(answer) > n[1]:
        heapq.heappop(answer)

print(sum(answer))