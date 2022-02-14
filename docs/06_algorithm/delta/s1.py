import sys

sys.stdin = open('input.txt', 'r')

N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 행
for i in range(0, N):
    # 열
    for j in range(0, N):
        # 해당인덱스에서 상하좌우 체크하기
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            # index 에러 방지
            if 0 <= ni < N and 0 <= nj < N:
                # 차이를 구한다
                minus_arr = arr[ni][nj] - arr[i][j]
                # 절대값을을더한다
                ans += abs(minus_arr)
                # if minus_arr < 0:
                #     result -= minus_arr
                # else:
                #     result += minus_arr
print(ans)