# 1389_케빈_베이컨의_6단계_법칙_문제풀이
# 2022-03-30

import sys
sys.stdin = open('input.txt', 'r')


def BFS(node):
    cnt = [0] * (N+1)
    front = -1
    rear = 0
    visited[node] = 1
    queue = [node]

    while front != rear:

        front += 1
        temp = queue[front]
        for t in Linked_lst[temp]:
            if visited[t] == 0:
                cnt[t] = cnt[temp] + 1
                queue.append(t)
                rear += 1
                visited[t] = 1

    return sum(cnt)


# 노드 / 간선 갯수
N, M = map(int, input().split())

# 연결 리스트
M_lst = [list(map(int, input().split())) for _ in range(M)]

Linked_lst = [[] for _ in range(N+1)]
for m in M_lst:
    Linked_lst[m[0]].append(m[1])
    Linked_lst[m[1]].append(m[0])

res = []
for n in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    ans = BFS(n)
    res.append(ans)

mim_ans = 101
min_index = 0
for i in range(N):
    if res[i] < mim_ans:
        mim_ans = res[i]
        min_index = i
print(min_index + 1)

