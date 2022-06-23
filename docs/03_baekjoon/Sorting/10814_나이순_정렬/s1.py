import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

N_lst = []
for i in range(N):
    age, name = map(str, input().split())
    N_lst.append([int(age), i, name])

N_lst.sort()

for n in N_lst:
    print('{} {}'.format(n[0], n[2]))