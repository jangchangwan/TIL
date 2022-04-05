# 1865_동철이의 일 분배 문제풀이
# 2022-03-31
import sys
sys.stdin = open('input.txt', 'r')


def DFS(i, cnt, ans):
    global max_ans
    # 결과값 비교
    if cnt == N:
        max_ans = max(max_ans, ans)
    # 작을 경우 탐색 종료
    if ans <= max_ans:
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            DFS(i + 1, cnt + 1, ans * (arr[i][j]/100))
            visited[j] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문체크
    visited = [0] * N
    max_ans = 0

    DFS(0, 0, 1)
    res = max_ans * 100
    print('#{} {:.6f}'.format(tc, res))