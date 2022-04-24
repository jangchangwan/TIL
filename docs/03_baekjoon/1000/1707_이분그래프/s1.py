# 1707_이분 그래프_문제풀이
# 2022-04-24

import sys
sys.stdin = open('input.txt', 'r')

'''
이분그래프란 집합을 둘로 나눴을때, 각 집합에 속한 정점끼리는 서로 인접하지않도록 분할할 수 있는 그래프
즉, 그래프 정점을 두가지 색으로 칠할 때, 인접한 정정끼리는 다른 색을 가지고 있는 그래프
BFS로 1 2 1 2 로 반복해서 채워나가면서 만약 조건에 맞지않을경우 No를 출력해보자
'''

def BFS(s):
    front = -1
    rear = 0
    queue = [s]
    # 겹치는거 방지
    if visited[s] == 0:
        visited[s] = 1
    while front != rear:
        front += 1
        temp = queue[front]
        check = visited[temp]

        for i in graph[temp]:
            if visited[i] == 0:
                queue.append(i)
                rear += 1
                # 반대색으로 넣어주기
                if check == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            # 1인경우 동일값이면 이분그래프 x
            elif visited[i] == 1:
                if check == 1:
                    print('NO')
                    return False
            # 2인경우 동일값 일경우
            elif visited[i] == 2:
                if check == 2:
                    print('NO')
                    return False
    return True


T = int(input())

for tc in range(T):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)
    ans = 0
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for k in range(1, V+1):
        if not BFS(k):
            ans = 1
            break

    if ans == 0:
        print('YES')
