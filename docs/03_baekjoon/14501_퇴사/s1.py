# 14510_퇴사_문제풀이
# 2022-03-23

import sys
sys.stdin = open('input.txt', 'r')


Day = int(input())

Day_lst = []
for i in range(Day):
    time, pay = map(int, input().split())
    Day_lst.append((time, pay))


cost = [0] * (Day + 1)

for i in range(Day-1, -1, -1):
    # 날짜를 초과하는 경우 그대로 앞으로 넘긴다
    if i + Day_lst[i][0] > Day:
        cost[i] = cost[i + 1]
    # 일할수 있는경우 상담 할경우와 안할경우 선택해서 큰 값 선택
    else:
        cost[i] = max(cost[i + 1], Day_lst[i][1] + cost[i + Day_lst[i][0]])
print(cost[0])
