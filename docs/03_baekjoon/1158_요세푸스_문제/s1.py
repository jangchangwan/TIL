import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

N_lst = [i for i in range(1, N+1)]

ans_lst = list()
i = 0
while len(N_lst):
    i = (i + K - 1) % len(N_lst)
    ans_lst.append(N_lst.pop(i))

print('<', end='')
for i in range(N):
    if i == (N-1):
        print(ans_lst[i],end='')
    else:
        print(ans_lst[i],end=', ')
print('>')

