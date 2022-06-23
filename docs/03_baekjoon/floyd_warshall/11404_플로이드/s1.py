# 11404_플로이드_문제풀이
# 2022-04-25

import sys
sys.stdin = open('input.txt', 'r')
'''

n 정점 : (2 ≤ n ≤ 100)
m 간선 :(1 ≤ m ≤ 100,000)개의 버스가 있다. 
각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을
'''



n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = int(1e9)

arr = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)

# 플로이드 와샬 알고리즘 적용
for k in range(n):
    arr[k][k] = 0
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

# 결과 출력
for row in arr:
    for i in range(n):
        # 갈 수 없는 경로인 경우, 0 출력
        if row[i] == inf:
            row[i] = 0
        print(row[i], end=" ")
    print()