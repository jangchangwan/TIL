# 2920_음계 문제풀이
# 2022-04-05
import sys
sys.stdin = open('input.txt', 'r')

num_lst = list(map(int, input().split()))

for i in range(len(num_lst)-1):
    if num_lst[i] - num_lst[i + 1] == -1:
        ans = 'ascending'
    elif num_lst[i] - num_lst[i + 1] == 1:
        ans = 'descending'
    else:
        ans = 'mixed'
        break
print(ans)