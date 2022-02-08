# [입력]

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

# [출력]
 
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

T = int(input())

for t in range(1,T+1):
    card_number = int(input())
    card_info = input()
    #0~9까지 행렬만들기
    cnt_list = [0]*10
    many_num = 0
    cnt = 0
    # 숫자에 해당하는 인덱스에  1씩 추가함 
    for num in card_info:
        cnt_list[int(num)] += 1

    many_cnt = 0
    # 반복문을 돌려 가장큰수 찾기
    for i in range(len(cnt_list)):
        # 동일한경우 큰숫자를 넣어줘야하므로 등호를 쓴다
        if cnt_list[i] >= many_cnt:
            many_num = i
            many_cnt = cnt_list[i]
        print(cnt_list[i])
    print('#{} {} {}'.format(t,many_num,many_cnt))