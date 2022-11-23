def BFS(maps, sr, sc, R, C):

    queue = [(sr, sc)]
    visited = [[0] * R  for _ in range(C)]
    visited[sr][sc] = 1

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    front = -1
    end = 0
    while front != end:
        front +=1
        r, c = queue[front]

        #  egcjrgiT
        if r == C-1 and c == R-1:
            return visited[r][c]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < C) and (0 <= nc < R) and visited[nr][nc] == 0 and maps[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                end += 1
                queue.append((nr,nc))

    # 못찾을 경우
    return -1