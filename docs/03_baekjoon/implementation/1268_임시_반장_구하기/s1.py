# 1268_임시반장구하기_문제풀이
# 2022-04-17

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
Class = [list(map(int, input().split())) for _ in range(N)]
Class_check = [[0]*N for _ in range(N)]
result = [0]*N

for i in range(5):
    for j in range(N):
        for k in range(j+1, N):
            if Class[j][i] == Class[k][i] and Class_check[j][k] == 0:
                Class_check[j][k] = 1
                Class_check[k][j] = 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if Class_check[i][j]:
            cnt += 1
    result[i] = cnt
banjang = result.index(max(result)) + 1
print(banjang)