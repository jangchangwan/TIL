# 4195_친구 네트워크
# 2022-06-16

def find(x):
    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]


T = int(input())

for tc in range(T):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])