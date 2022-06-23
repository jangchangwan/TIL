# 14889_스타트와_링크_문제풀이
# 2022-04-01
# 실패

import sys
sys.stdin = open('input.txt', 'r')


# 순서 출력
def find_order(n, picked, toPick):
    global temp_lst
    if toPick == 0:
        temp_lst.append(picked[:])
        return

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            find_order(n, picked, toPick - 1)
            picked.pop()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

order_lst = []
temp_lst = []
find_order(N, [], N//2)
for i in temp_lst:
    order_lst.append(i[:])
min_ans = 999999999999

temp_lst = []
find_order(N//2, [], 2)
for order in order_lst:

    temp = 0
    temp_2 = 0

    for i in temp_lst:
        temp += arr[order[i[0]]][order[i[1]]] + arr[order[i[1]]][order[i[0]]]
        temp_2 += arr[N-1-order[i[0]]][N-1-order[i[1]]] + arr[N-1-order[i[1]]][N-1-order[i[0]]]

    ans = abs(temp - temp_2)

    min_ans = min(min_ans, ans)

print(min_ans)