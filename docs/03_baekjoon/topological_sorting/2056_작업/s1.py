# 2056_작업
# 2022-06-23
# Pypy3 / 312 ms
'''
3 <= 작업 <= 10000
1 <= 작업시간 <= 100

선행 작업이 존재하는 작업들이 있다

모든 작업을 완료하기 위해 필요한 최소 시간


첫번째 줄 작업 수 N개
두번째 줄부터 작업에 대한 정보
작업시간, 선행작업 수, 선행작업에 대한 작업번호
'''

from collections import deque

# ------------------ 입력 -------------------
N = int(input())
graph = [[] for _ in range(N+1)]
cost = [0] * (N + 1)
indegree = [0] * (N + 1)
start_time = [0] * (N + 1)

for i in range(1, N+1):
    work = list(map(int, input().split()))
    cost[i] += work[0]
    indegree[i] += work[1]

    for j in work[2:]:
        graph[j].append(i)
# ------------------------------------------

answer = 0
queue = deque()
for i in range(1, N+1):
    # 선행조건이 없는 경우
    if indegree[i] == 0:
        queue.append((i, cost[i]))

while queue:
    now, time = queue.popleft()
    answer = max(answer, time)
    # 선행조건이 완료했으므로 indegree를 줄인다
    for new in graph[now]:
        indegree[new] -= 1
        start_time[new] = max(start_time[new], time)
        if indegree[new] == 0:
            queue.append((new, start_time[new] + cost[new]))

# 출력
print(answer)