# 1976_여행가자
# 2022-07-31
# 정답 X

# N이 200이하여서 가능한듯

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = 1
            arr[j][i] = 1

for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

check = True
for i in range(len(answer)-1):
    if arr[answer[i]-1][answer[i+1]-1] == 0:
        check = False
        break

if check:
    print('YES')
else:
    print('NO')