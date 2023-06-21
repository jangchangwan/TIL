"""
시작 (1, 1) 도착 (i, j)

범위는 N x M 이동방범은 나이트
"""
from pprint import pprint
def BFS():
    global arr
    queue = list()
    queue.append([N-1, 0])
    arr[N-1][0] = 1
    
    front = -1
    rear = 0
    
    
    while front != rear:
        front += 1
        r, c = queue[front]
        if r == N-1 - (er-1) and c == ec - 1:
            return arr[r][c] - 1
        
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            
            if (0 <= nr < N) and (0 <= nc < M) and arr[nr][nc] == 0:
                queue.append([nr, nc])
                arr[nr][nc] = arr[r][c] + 1
                rear += 1
        
    return "NEVER"
    
dir = [(-1, 2), (-2, 1), (1, 2), (2, 1), (1, -2), (2, -1), (-1, -2),(-2, -1)]

N, M, er, ec = map(int, input().split())

arr = [[0]*M for _ in range(N)]
answer = BFS()

print(answer)

