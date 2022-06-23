# 1202_보석도둑_문제풀이
# 2022-05-21

import sys
import heapq
sys.stdin = open('input.txt', 'r')


# 입력
# N : 보석갯수, K : 가방갯수
N, K = map(int, input().split())
# 보석 & 가방 데이터
N_lst = [list(map(int, input().split())) for _ in  range(N)]
K_lst = [int(input()) for _ in range(K)]

# 정렬
N_lst.sort()
K_lst.sort()

ans = 0

temp = []

for k in K_lst:
    while N_lst and k >= N_lst[0][0]:
        heapq.heappush(temp, -N_lst[0][1])
        heapq.heappop(N_lst)

    if temp:
        ans += heapq.heappop(temp)
    elif not N_lst:
        break


# 출력
print(-ans)


