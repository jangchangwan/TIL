

def DFS(here, depth):
    global flag, visited

    visited[here] = True
    if depth == 4:
        flag = True
        return
    for i in tree[here]:
        if not visited[i]:
            DFS(i, depth+1)
            visited[i] = False 

N, M = map(int, input().split())

flag = False
visited = [False]*2001
tree = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(N):
    DFS(i, 0)
    visited[i] = False
    if flag:
        break
if flag:
    print(1)
else:
    print(0)