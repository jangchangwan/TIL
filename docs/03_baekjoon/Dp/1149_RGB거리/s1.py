# 1149_RGB거리_문제풀이
# 2022-04-13

import sys
sys.stdin = open('input.txt', 'r')


'''
 N번집이 있을경우 앞뒤 색을 달라야한다.
 DFS로 선택된 색갈을 제외한 나머지 두곳에서 최소값을 구해서 더해주면서 간다.
 처음 선택지는 3곳이므로 3번 탐색해야한다.
'''

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])

print(min(arr[-1]))