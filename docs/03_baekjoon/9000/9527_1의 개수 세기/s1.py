# 9527_1의 개수 세기_문제풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt', 'r')

'''

1   1


10  1
11  2


100 1
101 2
110 2
111 3


1000    1
1001    2
1010    2
1011    3   
1100    2
1101    3
1110    3
1111    3

'''


def f(N):
    cnt = 0
    k = 0
    while 2**k <= N:
        temp = 2**(k+1)
        temp_cnt = (N+1)//temp
        # 완성된 패턴 수
        cnt += temp_cnt *(temp // 2)

        # 완성되지않은 길이
        ramain = (N+1) % temp
        cnt += max(0, ramain-temp // 2)
        k += 1
    return cnt


A, B = map(int, input().split())
print(f(B)-f(A-1))
