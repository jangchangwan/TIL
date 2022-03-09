import sys
sys.stdin = open('input.txt', 'r')


# stack 사용
def dfs_2(graph, v):
    global visited
    stack = [v]
    result = []
    # 더이상 갈곳이없을경우
    while stack:
        temp = stack.pop()
        if temp not in result:
            result.append(temp)
            stack.extend(graph[temp])
    return result


N, M, start_num = map(int, input().split())
# 서로간의 연관그래프 만들기
graph = [list() for _ in range(N+1)]
for m in range(M):
    start, end = map(int, input().split())
    # 양방향이므로 둘다 더해준다.
    graph[start].append(end)
    graph[end].append(start)

# 작은 수부터 탐색하기위해 정렬
for g in graph:
    g.sort(reverse=True)

ans = dfs_2(graph, start_num)
print(*ans)
for g in graph:
    g.sort()
bfs_list = [start_num]
x = min(N, M)
for i in range(x):
    temp = bfs_list[i]
    for s in graph[temp]:
        if s in bfs_list:
            continue
        bfs_list.append(s)
print(*bfs_list)

