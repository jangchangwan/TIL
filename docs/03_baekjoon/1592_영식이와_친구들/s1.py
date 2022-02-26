import sys
sys.stdin = open('input.txt', 'r')

N, M, L = map(int,input().split())
cnt = i = 0
user_lst = [0]*N
while M not in user_lst:
    if i >= N:
        i %= N
    user_lst[i] += 1
    i += L
    cnt += 1
print(cnt-1)