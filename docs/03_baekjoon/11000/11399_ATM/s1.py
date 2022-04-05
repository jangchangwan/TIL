import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
P_lst = list(map(int, input().split()))
P_lst.sort()
max_min = 0
now_min = 0
for p in P_lst:
    now_min += p
    max_min += now_min
print(max_min)