# 1932_정수_삼각형_문제풀이
# 2022-04-14

import sys
sys.stdin = open('input.txt', 'r')

'''
    양쪽끝을 제외하고는 둘중에서 큰값을 선택해서 가야한다.
    그러므로 0 , 끝값, 나머지를 고려해주며 진행하면  될것이다.
'''

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

k = 2
for i in range(1, N):
    for j in range(k):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i - 1][j]
        elif i == j:
            arr[i][j] = arr[i][j] + arr[i - 1][j - 1]
        else:
            arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + arr[i][j]
    k += 1
print(max(arr[N - 1]))
