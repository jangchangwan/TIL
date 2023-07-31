import sys


def check(n, m): 
  
    for d in range(6):
        nr = n + dr[d]
        nc = m + dc[d]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and seat[nr][nc]:
            visited[nr][nc] = True
            if connect[nr][nc] == [-1, -1] or check(connect[nr][nc][0], connect[nr][nc][1]):
                connect[nr][nc] = [n, m]       
                return True
    return False


input = sys.stdin.readline

dr = [0, 0, -1, -1, 1, 1]
dc = [-1, 1, -1, 1, -1, 1]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    
    seat = [[False] * M for _ in range(N)]
    answer = 0
    for n in range(N):
        for m in range(M):
            if arr[n][m] == '.':
                seat[n][m] = True
                answer += 1
                
    connect = [[[-1] * 2 for _ in range(M)] for __ in range(N)]
    for n in range(N):
        for m in range(0, M, 2):
            if seat[n][m]:
                visited = [[False] * M for _ in range(N)]
                if check(n, m):
                    answer -= 1
    print(answer)