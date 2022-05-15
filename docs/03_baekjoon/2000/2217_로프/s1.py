# 2217_로프_문제풀이
# 2022-05-14

import sys
sys.stdin = open('input.txt', 'r')
'''
처음줄이 최대인경우 15 x 1
두번쨰줄이 최대인경우 10 x 2
즉
n번쨰 줄이 최대인경우 N_Value X N
=> 역순으로 정렬후 값의 최대값 출력
'''
N = int(input())

N_lst = list(int(input()) for _ in range(N))
N_lst.sort(reverse=True)

ans = []
for n in range(N):
    ans.append(N_lst[n] * (n+1))

print(max(ans))
