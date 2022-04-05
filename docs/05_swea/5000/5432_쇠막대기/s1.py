# 5432_쇠막대기_자르기_문제풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    bar_list = list(input())
    # () 가 만날경우 레이저 발사 기본에 있던 막대갯수를 ans 더해주기
    # ( 일경우 막대기 1개증가
    # ) 일경우 막대가 1개 감소  , ans 1씩 더해주기
    stick = 0
    result = 0
    for i in range(len(bar_list)):
        # ( 인 경우
        if bar_list[i] == '(':
            stick += 1
        # ) 인 경우
        else:
            # 앞이 ( 인 경우
            if bar_list[i-1] == '(':
                stick -= 1
                result += stick
            # 앞이 ) 인 경우
            else:
                stick -= 1
                result += 1

    ans = result
    print('#{} {}'.format(t, ans))