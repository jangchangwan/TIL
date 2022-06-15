from collections import deque

def BFS(arr, answer):
    N = len(arr)
    dist = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(4)]
    queue = deque()
    # 시작시 오른쪽 & 아래 시작 두가지 경우 추가
    queue.append([0, 0, 0, 0])
    queue.append([0, 0, 0, 1])
    while queue:
        r, c, cost, dir = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N) and arr[nr][nc] == 0:
                ncost = cost + 1
                if dir != direction[d]:
                    ncost += 5

                if dist[direction[d]][nr][nc] > ncost:
                    dist[direction[d]][nr][nc] = ncost
                    if nr == N-1 and nc == N-1:
                        continue
                    queue.append([nr, nc, ncost, direction[d]])
    for i in range(4):
        answer = min(answer, dist[i][N-1][N-1])
    answer *= 100
    return answer


direction = [0, 1, 2, 3]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
INF = 987654321

def solution(board):
    answer = INF
    answer = BFS(board, answer)
    print(answer)
    return answer


solution([[0,0,0],[0,0,0],[0,0,0]])