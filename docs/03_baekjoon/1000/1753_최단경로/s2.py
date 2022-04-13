# 백준 1753 최단경로 힙x
import sys

INF = 999999999
# 입력
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
route = {}
cost = {}
not_visit = {}
for i in range(e):
    node, to, value = map(int, sys.stdin.readline().split())
    if node in route:
		route[node] += [[to, value]]
	else:
		route[node] = [[to, value]]
	# 초기화

for i in range(1, v + 1):
	cost[i] = INF
	not_visit[i] = True

cost[k] = 0
while not_visit.keys():
	min_cost = INF + 1
	min_index = 0
	for node in not_visit.keys():  # 가장 최소비용의 노드 찾는 중
		if cost[node] < min_cost:
			min_cost = cost[node]
			min_index = node
	del not_visit[min_index]
	if min_index in route:
		for info in route[min_index]:
			if cost[info[0]] > info[1] + cost[min_index]:
				cost[info[0]] = info[1] + cost[min_index]
# 출력
for i in range(1, v + 1):
	if cost[i] == INF:
		print("INF")
	else:
		print(cost[i])