# 1145_적어도_대부분의_배수_문제풀이
# 2022-04-15

import sys
sys.stdin = open('input.txt','r')

'''
자연수 5개가 100보다 작은수이므로 범위가 작으므로
4부터시작해서 3개의숫자가 나누어질경우 숫자를 출력하면 될것같다
'''


N_lst = list(map(int, input().split()))

K = 4

while True:
    cnt = 0
    for n in N_lst:
        if K % n == 0:
            cnt += 1
    if cnt >= 3:
        break
    K += 1
print(K)