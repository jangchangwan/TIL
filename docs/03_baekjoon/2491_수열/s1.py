import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

num_list = list(map(int, input().split()))

cnt = 1
max_1 = 1
for i in range(N-1):
    if num_list[i] >= num_list[i+1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > max_1:
        max_1 = cnt


cnt = 1
for i in range(N-1):
    if num_list[i] <= num_list[i+1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > max_1:
        max_1 = cnt

print(max_1)