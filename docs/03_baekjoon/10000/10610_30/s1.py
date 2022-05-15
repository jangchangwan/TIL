# 10610_30_문제풀이
# 2022-05-14

import sys
sys.stdin = open('input.txt', 'r')

number = list(input())
number.sort(reverse=True)

sum_number = 0
for i in number:
    sum_number += int(i)
if sum_number % 3 != 0 or "0" not in number:
    print(-1)
else:
    print(''.join(number))