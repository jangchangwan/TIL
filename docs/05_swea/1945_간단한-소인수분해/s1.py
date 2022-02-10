import sys

sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T+1):
    num = int(input())
    # 소인수분해할 숫자를 리스트로 할당한다
    n_list = [2, 3, 5, 7, 11,12]

    # while 문을 쓰기 위해 인덱스 설정
    i = 0
    # 결과를 넣을 변수 설정
    cnt = 0
    cnt_list = [0] * 5
    while n_list[i] <= num:
        # 나머지가 0 이 되는경우 그 횟수를 카운팅한다.
        if num % n_list[i] == 0:
            num = num // n_list[i]
            cnt += 1
        # 나머지가 0 이아닌경우 다음 인덱스로 넘어가고 다시 카운팅한다.
        else:
            cnt_list[i] = cnt
            i += 1
            cnt = 0
    # 마지막은 else 를 안거치기 때문에 추가로 한줄 더 써야한다.
    cnt_list[i] = cnt

    print('#{}'.format(t), end=' ')
    for i in range(4):
        print(cnt_list[i], end=' ')
    print(cnt_list[4])
