# 1598_꼬리를 무는 숫자 나열
# 2022-07-12

from pprint import pprint

N, M = map(int, input().split())

max_value = max(N, M) // 4 + 1

arr = [[0] * max_value for _ in range(4)]
value = 1
res = []
for j in range(max_value):
    for i in range(4):
        arr[i][j] = value
        if arr[i][j] == N or arr[i][j] == M:
            res.append((i, j))
        value += 1


answer = abs(res[0][0] - res[0][1]) + abs(res[1][0] - res[1][1])
print(answer)