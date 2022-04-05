import sys
sys.stdin = open('input.txt', 'r')


# 스타트는 1
def dfs(graph):
    stack = [1]
    visited = []
    while stack:
        temp = stack.pop()
        if temp not in visited:
            visited.append(temp)
            stack.extend(graph[temp])
    return len(visited)


computer = int(input())
link = int(input())

# 연결리스트
link_list = [[] for _ in range(computer+1)]
for tc in range(link):
    start, end = map(int, input().split())
    link_list[start].append(end)
    link_list[end].append(start)

ans = dfs(link_list)
print(ans-1)