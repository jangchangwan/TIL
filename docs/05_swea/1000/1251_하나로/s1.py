# 1251_하나로_문제풀이
# 2022-04-06
import sys
sys.stdin = open('input.txt', 'r')


def prim(s):
    global result

    key = [INF] * N
    key[s] = 0
    visited = [0] * N
    for _ in range(N):
        min_idx = -1
        min_val =INF
        for i in range(N):
            if visited[i] == 0 and key[i] < min_val:
                min_val = key[i]
                min_idx = i

        visited[min_idx] = 1
        print(w_arr[min_idx])
        for v, val in w_arr[min_idx]:
            if visited[v] == 0 and key[v] > val:
                key[v] = val

        return key



INF = 100000000
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    r_lst = list(map(int, input().split()))
    c_lst = list(map(int, input().split()))

    # E = L ** 2
    E = float(input())
    # 가중치 배열
    w_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            w_arr[i][j] = (r_lst[i] - r_lst[j]) ** 2 + (c_lst[i] - c_lst[j]) ** 2
            w_arr[j][i] = w_arr[i][j]

    key = prim(0)
    print(sum(key))
