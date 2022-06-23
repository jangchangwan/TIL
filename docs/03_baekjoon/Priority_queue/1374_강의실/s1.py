# 1374_강의실_문제풀이
# 2022-06-04

import sys
import heapq
sys.stdin = open('input.txt', 'r')

N = int(input())

heap = []
queue = []
for _ in range(N):
    num, start, end = map(int, input().split())
    heapq.heappush(heap, [start, end, num])

start, end, num = heapq.heappop(heap)
heapq.heappush(queue, end)

while heap:
    start, end, num = heapq.heappop(heap)
    if queue[0] <= start:
        heapq.heappop(queue)
    heapq.heappush(queue, end)

print(len(queue))