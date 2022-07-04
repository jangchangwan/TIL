# 1927_최소 힙
# 2022-07-04

import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    number = int(input())
    if number:
        heapq.heappush(heap, number)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)