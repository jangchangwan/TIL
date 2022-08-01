# 1976_여행가자
# 2022-08-02

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x


N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = list(map(int, input().split()))

parent = [i for i in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            pi = find(i)
            pj = find(j)
            if pi < pj:
                parent[pj] = pi
            else:
                parent[pi] = pj


root = parent[answer[0]-1]
for p in answer:
    if root != parent[p-1]:
        print("NO")
        exit(0)

print("YES")