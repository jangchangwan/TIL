from pprint import pprint

 
def BFS(rr, rc, br, bc):
    queue = list()
    queue.append((rr, rc, br, bc))
    visited = []
    visited.append((rr, rc, br, bc))
    count = 0
    
    front = -1
    rear = 0
    while front != rear:

        front += 1
        for _ in range(len(queue[front:])):
            rx, ry, bx, by = queue[front]
            
            # 종료조건
            if count > 10:
                return -1
            if arr[rx][ry] == 'O':
                return count 
              
            # 실행
            for i in range(4):
                nrx, nry = rx, ry
                while True: 
                    nrx += dr[i]
                    nry += dc[i]
                    if arr[nrx][nry] == '#': 
                        nrx -= dr[i]
                        nry -= dc[i]
                        break
                    if arr[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dr[i]
                    nby += dc[i]
                    if arr[nbx][nby] == '#': 
                        nbx -= dr[i]
                        nby -= dc[i]
                        break
                    if arr[nbx][nby] == 'O':
                        break
                if arr[nbx][nby] == 'O': 
                    continue
                if nrx == nbx and nry == nby: 
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dr[i]
                        nry -= dc[i]
                    else:
                        nbx -= dr[i]
                        nby -= dc[i]
                if (nrx, nry, nbx, nby) not in visited: 
                    rear += 1
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    return -1
 

N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1 ,1]

for i in range(N):
    for j in range(M):  
        if arr[i][j] == "R":
            rr, rc = i, j
        elif arr[i][j] == "B":
            br, bc = i, j

          
          
answer = BFS(rr, rc, br, bc)

print(answer)