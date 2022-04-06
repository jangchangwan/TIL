# 10989_수 정렬하기 3 문제풀이
# 2022-04-06
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

N_dic = {}
for _ in range(N):
    num = int(input())

    if num in N_dic:
        N_dic[num] += 1
    else:
        N_dic[num] = 1

sort_N = sorted(N_dic.items())

for i in range(len(sort_N)):
    for j in range(sort_N[i][1]):
        print(sort_N[i][0])
