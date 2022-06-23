# 16562_친구비
# 2022-06-14

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M, K = map(int, input().split())

friends = list(map(int, input().split()))
parent = [i for i in range(N + 1)]


for _ in range(M):
    v, w = map(int, input().split())
    union_parent(parent, v, w)


answer = 0
visited = set()
for i in range(1, N + 1):
    if i not in visited:
        temp = [i]
        cost = friends[i - 1]
        for j in range(1, N + 1):
            if i != j:
                if find_parent(parent, i) == find_parent(parent, j):
                    temp.append(j)
                    cost = min(cost, friends[j - 1])
        visited.update(temp)
        answer += cost

if K >= answer:
    print(answer)
else:
    print("Oh no")