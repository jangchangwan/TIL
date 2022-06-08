# 1182부분수열의 합2_문제풀이
# 2022-06-08


def DFS(idx, total):
    global cnt
    if idx == N:
        return

    total += N_lst[idx]
    if total == S:
        cnt += 1

    DFS(idx+1, total)
    DFS(idx+1, total-N_lst[idx])


# 입력
N, S = map(int, input().split())
N_lst = list(map(int, input().split()))
cnt = 0

DFS(0, 0)
# 출력
print(cnt)
