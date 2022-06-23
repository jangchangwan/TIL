# 14003_가장 긴 증가하는 부분 수열 5_문제풀이
# 2022-06-10


import bisect
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

table = []
idx = []

for i in arr:
    if not table or i > table[-1]:
        table.append(i)
        idx.append(len(table) - 1)
    else:
        j = bisect.bisect_left(table, i)
        table[j] = i
        idx.append(j)

lth = len(table)
print(lth)
seq = []
for i in range(len(idx)-1, -1, -1):
    if lth == 0: break
    if lth - 1 == idx[i]:
        seq.append(arr[i])
        lth -= 1
print(*seq[::-1])