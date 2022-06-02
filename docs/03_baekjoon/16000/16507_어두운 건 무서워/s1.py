# 16507_어두운 건 무서워_문제풀이
# 2022-05-23
# 누적합
import sys
sys.stdin = open('input.txt', 'r')





N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
temp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        temp[i][j] =


# 코드가 생각이안나

for _ in range(K):
    sr, sc, er, ec = map(int, input().split())
    bright = 0


    print(bright)
