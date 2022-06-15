from collections import deque


def BFS(place):
    start = []
    # 사람이 앉아 있는 곳 찾기
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i, j])


    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0] * 5 for i in range(5)]  # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1

        while queue:
            r, c = queue.popleft()



            for i in range(4):
                nr = x + dr[i]
                nc = y + dc[i]

                if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] == 0:

                    if p[nr][nc] == 'O':
                        queue.append([nr, nc])
                        visited[nr][nc] = 1
                        distance[nr][nc] = distance[r][c] + 1

                    if p[nr][nc] == 'P' and distance[r][c] <= 1:
                        return 0
    return 1


dr = [-1, 1, 0, 0]  # 좌우
dc = [0, 0, -1, 1]  # 상하

def solution(places):
    answer = []

    for place in places:
        answer.append(BFS(place))

    return answer