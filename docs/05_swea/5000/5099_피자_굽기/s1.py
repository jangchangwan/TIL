# 5099_피자_굽기_문제풀이
# 2022-03-15
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    size, pizza = map(int, input().split())
    pizza_lst = list(map(int, input().split()))

    new_pizza_list = list()
    # pizza 마다 index 추가
    for p in range(1, pizza+1):
        new_pizza_list.append([p, pizza_lst[p-1]])
    # 먼저 화구에 들어갈 피자
    in_pizza_lst = new_pizza_list[:size]
    # pop(0) 안쓸려는 몸부림
    # 남아 있는 피자
    out_pizza_lst = new_pizza_list[size:]
    out_pizza_lst = out_pizza_lst[::-1]
    front = -1
    rear = 0
    cnt = 0
    while cnt != pizza:
        front += 1
        temp = in_pizza_lst[front]
        temp[1] //= 2
        # 치즈가 0이되면 교체
        if temp[1] == 0:
            if len(out_pizza_lst) != 0:
                in_pizza_lst.append(out_pizza_lst.pop())
                rear += 1
            else:
                rear += 1
            # 0인 경우가 총 pizza 갯수만큼 반복시 종료
            cnt += 1
        # 0이 아닐경우 다시 집어넣는다
        else:
            in_pizza_lst.append(temp)
            rear += 1
        print(in_pizza_lst)
    # 마지막 피자 인덱스 출력
    print('#{} {}'.format(tc, temp[0]))



