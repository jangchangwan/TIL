# 10819 차이를 최대로
# 2022-06-28
# 백트래킹

def Back_tracking(n, num, sum_num, visited):
    global max_ans
    if n == N:
        max_ans = max(sum_num, max_ans)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            Back_tracking(n+1, i, sum_num + abs(arr[num] - arr[i]), visited)
            visited[i] = 0


N = int(input())
arr = list(map(int, input().split()))

visited = [0] * N
max_ans = -200 * N

for i in range(N):
    visited[i] = 1
    Back_tracking(1, i, 0, visited)
    visited[i] = 0

print(max_ans)