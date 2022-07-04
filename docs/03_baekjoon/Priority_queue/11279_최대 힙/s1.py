# 11279_최대 힙
# 2022-07-04

import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    number = int(input())
    if number:
        heapq.heappush(heap, (-number, number))
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)