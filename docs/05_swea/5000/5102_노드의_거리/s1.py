# 5102_노드의거리_문제풀이
# 2022-03-15

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 노드와 간선 개수
    V, E = map(int, input().split())

    # 연결 리스트
    arr = [[] for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        arr[start].append(end)
        arr[end].append(start)

    # 시작, 도착
    start, end = map(int, input().split())

    # 방문 체크
    visited = [0] * (V+1)
    
    # BFS 시작
    queue = [start]     # 시작을 처음에 넣어준다
    visited[start] = 1  # 방문 처리
    front = -1          # 시작
    rear = 0            # 끝
    ans = 0             # 횟수
    # 처음과 끝이 만나는 경우 종료
    while front != rear:
        front += 1
        temp = queue[front]
        for i in arr[temp]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[temp] + 1
                rear += 1

        # end 가 안에 있을 경우
        if end in queue:
            ans = visited[temp]
            break
    print('#{} {}'.format(tc, ans))
