# 4875_미로_문제풀이
# 2022-02-24
import sys
sys.stdin = open('input.txt', 'r')


# 위치 탐색 함수 (출발점 찾기위한 인덱스)
def find_location(arr, K):
    global N
    for i in range(N):
        for j in range(N):
            if arr[i][j] == K:
                return i, j


# 이동 함수
def dfs(row, col):
    global result
    stack = [(row, col)]
    # 스택이 빌 때까지 작동
    while stack:
        # 도착했을 경우 1로 반환
        graph_rc = stack.pop()
        # 방문했을경우 확인을 위해 1로 변경
        arr[graph_rc[0]][graph_rc[1]] = 1
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        # 4방향 탐색
        for i in range(4):
            new_row = graph_rc[0] + dr[i]
            new_col = graph_rc[1] + dc[i]
            # 범위 체크
            if (0 <= new_row < N) and (0 <= new_col < N):
                # 방문 안한곳일 경우 간다
                if arr[new_row][new_col] == 0:
                    stack.append((new_row, new_col))
                # 도착점일 경우 결과를 1로 리턴받고 빠저나온다
                elif arr[new_row][new_col] == 3:
                    result = 1
                    return


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    result = 0
    # 시작점 찾기
    row, col = find_location(arr, 2)
    # dfs 동작
    dfs(row, col)

    ans = result
    print('#{} {}'.format(t, ans))