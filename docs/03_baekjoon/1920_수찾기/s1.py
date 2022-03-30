# 1920_수-찾기_문제풀이
# 2022-03-30
# 시간초과
import sys
sys.stdin = open('input.txt', 'r')

# 있는 정수
N = int(input())
N_lst = list(map(int, input().split()))
# 있는지 탐색할 숫자
M = int(input())
M_lst = list(map(int, input().split()))


for i in range(M):
    if M_lst[i] in N_lst:
        print(1)
    else:
        print(0)