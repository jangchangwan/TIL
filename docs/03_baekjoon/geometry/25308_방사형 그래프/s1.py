# 25308_방사형 그래프
# 2022-06-25
# 기하학
import math

def back_tracking(arr, N, visited):
    global cnt
    # 3개부터는 오목한지 확인 시작
    if N >= 3:
        a = arr[-2] * math.sin(math.pi * (45 / 180))
        b = arr[-3] - arr[-2] * math.sin(math.pi * (45 / 180))
        # 처음점과 두번쨰 점과의 각도
        drgree_1 = math.atan(b/a)
        # 처음점과 세번째 점과의 각도
        drgree_2 = math.atan(arr[-3]/arr[-1])

        # 오목할 경우
        if drgree_1 > drgree_2:
            return
    # 종료조건
    if N == 8:
        a = arr[-1] * math.sin(math.pi * (45 / 180))
        b = arr[-2] - arr[-1] * math.sin(math.pi * (45 / 180))
        # 처음점과 두번쨰 점과의 각도
        drgree_1 = math.atan(b / a)
        # 처음점과 세번째 점과의 각도
        drgree_2 = math.atan(arr[-2] / arr[0])
        # 오목할 경우
        if drgree_1 > drgree_2:
            return
        a = arr[0] * math.sin(math.pi * (45 / 180))
        b = arr[-1] - arr[0] * math.sin(math.pi * (45 / 180))
        # 처음점과 두번쨰 점과의 각도
        drgree_1 = math.atan(b / a)
        # 처음점과 세번째 점과의 각도
        drgree_2 = math.atan(arr[-1] / arr[1])
        # 오목할 경우
        if drgree_1 > drgree_2:
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