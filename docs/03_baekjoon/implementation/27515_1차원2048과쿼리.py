import sys
import math
input = sys.stdin.readline

Q = int(input())

jisoo_list = [0] * 64
for _ in range(Q):
    Query = input()
    # Query[0] == 0 인 경우 Query[1:]가 빈문자열이 되므로 
    # 아래 해당하는 if문을 기입하지 않을시 valueerror가 발생합니다.
    if Query[1] == '0':
        pass
    elif Query[0] == '+':
        # log 사용시 실수로 변환되므로 정수로 변환시켜줘야 한다.
        jisoo_list[int(math.log2(int(Query[1:])))] += 1
    elif Query[0] == '-':
        jisoo_list[int(math.log2(int(Query[1:])))] -= 1

    pre = 0 # 이전 값
    value = -1 # 지수 값

    for i in range(64):
        # 값이 있는경우
        if jisoo_list[i] + pre:
            pre = (jisoo_list[i] + pre) // 2
            value = i
        else:
            pre = 0
    
    # 값이 없는 경우
    if value < 0:
        print(0)
    else:
        print(2 ** value)

