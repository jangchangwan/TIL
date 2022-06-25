# 25308_방사형 그래프
# 2022-06-25
# 실패??
import math


def back_tracking(arr, N, visited):
    global cnt
    # 3개부터는 오목한지 확인 시작
    if N >= 3:
        c = math.sqrt(arr[-3]**2 + arr[-1]**2)
        h = (arr[-3] * arr[-1]) / c
        # 오목할 경우
        if arr[-2] <= h:
            return
    # 종료조건
    if N == 8:
        c = math.sqrt(arr[-2] ** 2 + arr[0] ** 2)
        h = (arr[-2] * arr[0]) / c
        # 오목할 경우
        if arr[-1] <= h:
            return
        c = math.sqrt(arr[-1] ** 2 + arr[1] ** 2)
        h = (arr[-1] * arr[1]) / c
        # 오목할 경우
        if arr[0] <= h:
            return
        cnt += 1
        return
    else:
        for i in range(8):
            # 갔던 곳은 재탐색 X
            if visited[i] == 0:
                visited[i] = 1
                back_tracking(arr + [N_lst[i]], N+1, visited)
                visited[i] = 0


N_lst = list(map(int, input().split()))
visited = [0]*8

cnt = 0
for i in range(8):
    visited[i] = 1
    back_tracking([N_lst[i]], 1, visited)
    visited[i] = 0

print(cnt)