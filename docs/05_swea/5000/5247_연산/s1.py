# 5247_연산_문제풀이
# 2022-04-01

import sys
sys.stdin = open('input.txt', 'r')


def BFS(s, e):
    global visited
    front = -1
    rear = 0
    visited[s] = 1
    queue = [s]
    while front != rear:
        front += 1
        temp = queue[front]
        # 목표점에 도달할경우
        if temp == e:
            return visited[temp]

        for i in range(4):
            # 수식 4개 동작
            # 1 더하기
            if i == 0:
                ni = temp + 1
            # 1 빼기
            elif i == 1:
                ni = temp - 1
            # 2 곱하기
            elif i == 2:
                ni = temp * 2
            # 10 빼기
            else:
                ni = temp - 10
            # 범위내에서만 동작 and 갔던곳은 또 갈 필요 X
            if (0 < ni <= 1000000) and visited[ni] == 0:
                visited[ni] = visited[temp] + 1
                queue.append(ni)
                rear += 1
    # 못찾은 경우
    return -1


T = int(input())

for tc in range(1, T+1):
    start, end = map(int, input().split())
    visited = [0] * 1000001
    # 시작점부터 1로 시작했으므로 1을 빼줘야 한다
    ans = BFS(start, end) - 1

    print('#{} {}'.format(tc, ans))