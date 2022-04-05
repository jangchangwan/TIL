# 1225_암호생성기_문제풀이
# 2022-02-25
import sys
sys.stdin = open('input.txt', 'r')

T = 10

for t in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    i = 1
    # while 문 초기 한번 실행하기위해서 추가
    num = 1
    
    # num 가 0일 때 종료
    while num:
        # 5가 넘어갈 경우 다시 1로
        if i > 5:
            i = 1
        # 맨앞 값에 i 을 뺀값을 저장
        num = N_list.pop(0) - i
        # 0이하로 될경우 0으로 변경
        if num < 0:
            num = 0
        # 값을 맨뒤로 넣는다
        N_list.append(num)
        i += 1

    print('#{}'.format(t), end=' ')
    for n in N_list:
        print(n, end=' ')
    print()
