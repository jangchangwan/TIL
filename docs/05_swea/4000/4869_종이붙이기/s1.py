# 4869_종이붙이기_문제풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')


def paper_cutting(n):
    global bax_case
    # 이전에 했던 결과의 길이가 구하고자하는 n 값보다 작을경우
    if n >= len(bax_case):
        for i in range(len(bax_case), n+1):
            bax_case.append(bax_case[i-1] + (bax_case[i-2] * 2))


T = int(input())
# 경우의수 0,1,2 초기값을 설정해준다.
bax_case = [0, 1, 3]
for t in range(1, T+1):
    N = int(input())
    num = N // 10
    paper_cutting(num)
    # num 번째 경우의수 출력
    ans = bax_case[num]
    print('#{} {}'.format(t, ans))