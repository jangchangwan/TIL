# 10867_중복 빼고 정렬하기
# 2022-05-11

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
N_lst = list(map(int, input().split()))
data = set()
for n in N_lst:
    data.add(n)

data = sorted(list(data))
print(*data)