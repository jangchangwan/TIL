from collections import deque
# 611 ms / 16.3 MB


class Solution:
    def bfs(self, sr, sc, grid, visited):
        N = len(grid)
        M = len(grid[0])
        visited[sr][sc] = 1
        queue = deque()
        queue.append([sr, sc])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N) and (0 <= nc < M) and grid[nr][nc] == "1" and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])

    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        visited = [[0 for i in range(M)] for j in range(N)]

        ans = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    ans += 1
                    self.bfs(i, j, grid, visited)
        return ans