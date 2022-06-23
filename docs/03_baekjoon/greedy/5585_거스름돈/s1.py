# 5585_거스름돈_문제풀이
# 2022-05-14

import sys
sys.stdin = open('input.txt', 'r')

# 지불한 금액
money = int(input())
# 거스름돈
res = 1000 - money
# 동전 갯수
ans = 0
money_list = [500, 100, 50, 10, 5]

for m in money_list:
    if res // m:
        ans += (res // m)
        res %= m

ans += res
print(ans)