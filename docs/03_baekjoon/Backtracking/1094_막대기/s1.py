# 1094_막대기
# 2022-07-01
# 백트래킹

def back_tracking(total, cnt, visited):
    if total == X:
        print(cnt)
        exit()

    for x in X_lst:
        if visited[x] == 0:
            visited[x] = 1
            back_tracking(total+x, cnt+1, visited)
            back_tracking(total, cnt, visited)
            visited[x] = 0


X = int(input())

N_lst = [1, 2, 4, 8, 16, 32, 64]
X_lst = []
# 사용 가능한 막대기만 찾기
for n in N_lst:
    if n > X:
        continue
    X_lst.append(n)


visited = [0] * 65
for x in X_lst:
    visited[x] = 1
    back_tracking(x, 1, visited)
    visited[x] = 0

back_tracking()

