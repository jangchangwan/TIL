import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
# 좌표끝에 붙었을 때도 길이 파악하기위해서
N_arr = [[0]*102 for _ in range(102)]

# 색종이 덮기
for n in range(N):
    col, row = map(int, input().split())
    for i in range(row, row+10):
        for j in range(col, col+10):
            N_arr[i+1][j+1] = 1
# 방향
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(4):
            ni = i + dir[k][0]
            nj = j + dir[k][1]
            if (1 <= ni < 102) and (1 <= ni < 102) and (N_arr[i][j] == 1) and (N_arr[ni][nj] == 0):
                cnt += 1
print(cnt)


