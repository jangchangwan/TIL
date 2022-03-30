import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

N_lst = list()
for n in range(N):
    N_lst.append(input())
# 중복제거
N_lst = list(set(N_lst))
ans_lst = []
for i in N_lst:
    ans_lst.append((len(i), i))

ans_lst.sort()


for i in ans_lst:
    print(i[1])