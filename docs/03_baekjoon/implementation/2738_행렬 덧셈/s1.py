# 2738_행렬 덧셈_문제풀이
# 2022-06-05


# 행렬 크기 N, M
N, M = map(int, input().split())
# 행렬 데이터 받기
N_arr = [list(map(int, input().split())) for _ in range(N)]
M_arr = [list(map(int, input().split())) for _ in range(N)]

# 결과를 담을 행렬 만들기
ans_arr = [[0]*M for _ in range(N)]
# 행렬 합치기
for i in range(N):
    for j in range(M):
        ans_arr[i][j] = N_arr[i][j] + M_arr[i][j]

# 행렬 출력
for ans in ans_arr:
    print(*ans)