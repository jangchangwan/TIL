# 1859_백만장자_프로젝트_문제풀이
# 2022-02-17
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    day_num = int(input())
    price = list(map(int, input().split()))
    # 마지막날
    max_price = price[-1]
    profit = 0
    # 0까지 동작
    for i in range(len(price)-1, -1, -1):
        # 전날이랑 비교해서 클경우
        if max_price > price[i]:
            # 그차이만큼 이익에 추가한다
            profit += max_price - price[i]
        # 아닐경우 높은값을 변경해준다
        else:
            max_price = price[i]
    ans = profit
    print('#{} {}'.format(t, ans))