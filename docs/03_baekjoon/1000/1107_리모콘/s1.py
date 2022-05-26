# 1107_리모콘_문제풀이
# 2022-05-26

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())

if M:
    M_lst = list(map(int, input().split()))
else:
    M_lst = []

# 채널 100에서 시작하므로 최대값
min_ans = abs(N - 100)

# 범위를 100만으로 한이유
# 40만에서 시작해서 50만까지갔을경우보다
# 53만에서 50만 가는 경우가 최적해에 가깝기때문에
# 최대 100만까지는 돌려야할것이다.

for num in range(0, 1000001):
    num = str(num)

    for j in range(len(num)):
        # check
        if int(num[j]) in M_lst:
            break
        elif j == len(num) - 1:
            min_ans = min(min_ans, abs(int(num) - N) + len(num))

print(min_ans)