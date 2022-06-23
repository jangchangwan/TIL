# 9663_N-Queen-문제풀이
# 2022-03-05
# 시간초과
import sys
sys.stdin = open('input.txt', 'r')


def back_T(n):
    global cnt
    if n == N:
        cnt += 1
    else:
        for i in range(N):
            base_arr[n] = i
            # 대각선
            if check(n):
                back_T(n+1)


def check(n):
    for i in range(n):
        if (base_arr[i] == base_arr[n]) or ((n - i) == abs(base_arr[n] - base_arr[i])):
            return 0
    return 1
            

N = int(input())

base_arr = [0] * N
cnt = 0
back_T(0)
print(cnt)