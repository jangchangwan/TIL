import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    card_number = int(input())
    card_info = input()
    # 0~9 까지 행렬 만들기
    cnt_list = [0]*10
    cnt = 0
    # 숫자에 해당하는 인덱스에  1씩 추가함
    for num in card_info:
        cnt_list[int(num)] += 1

    many_cnt = cnt_list[0]
    # 반복문을 돌려 가장큰수 찾기
    for i in range(10):
        # 동일한경우 큰숫자를 넣어줘야하므로 등호를 쓴다
        if cnt_list[i] >= many_cnt:
            many_num = i
            many_cnt = cnt_list[i]
            # print('many_cnt : ',many_cnt)
            # print('many_num : ',many_num)
        # print(cnt_list[i])
    print('#{} {} {}'.format(t, many_num, many_cnt))