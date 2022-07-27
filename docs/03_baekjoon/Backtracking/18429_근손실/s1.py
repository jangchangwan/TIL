# 18429_근손실
# 2022-07-27
# Python3 30840KB / 140 ms

def DFS(day, power):
    global cnt, visited

    # 500 이하로 떨어진 경우
    if power < 500:
        return

    # 종료조건
    if day == N:
        cnt += 1
        return

    # 백트래킹
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            DFS(day+1, power+arr[i]-K)
            visited[i] = 0


# 입력
N, K = map(int, input().split())
arr = list(map(int, input().split()))

visited = [0] * N
cnt = 0

DFS(0, 500)
# 출력
print(cnt)