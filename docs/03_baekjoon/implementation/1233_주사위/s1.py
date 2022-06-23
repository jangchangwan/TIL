# 1233_주사위_문제풀이
# 2022-04-16

import sys
sys.stdin = open('input.txt', 'r')

A, B, C = map(int, input().split())

visited = [0] * (A + B + C + 1)
for a in range(1, A+1):
    for b in range(1, B+1):
        for c in range(1, C+1):
            visited[a+b+c] += 1

print(visited.index(max(visited)))