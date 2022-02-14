import sys
sys.stdin = open('input.txt', 'r')
N = 5
arr = [[0]*7] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*7] # 테두리를 0으로 씌운다!
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # 상 하 좌 우 탐색
            ni = i + di
            nj = j + dj
            if arr[ni][nj] != 0: # 0인경우는 제외!
                ans += abs(arr[ni][nj] - arr[i][j])
print(ans)