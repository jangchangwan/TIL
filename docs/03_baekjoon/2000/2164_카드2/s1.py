# 2164_카드2_문제풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

N_lst = [i for i in range(1, N+1)]

front = 0
rear = N-1

while front != rear:
    # 삭제
    front += 1
    # 뒤로 보내기
    N_lst.append(N_lst[front])
    front += 1
    rear += 1

print(N_lst[front])