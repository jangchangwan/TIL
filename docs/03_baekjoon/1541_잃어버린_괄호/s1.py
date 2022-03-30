# 1541_잃어버린-괄호-문제풀이
# 2022-03-30

import sys
sys.stdin = open('input.txt', 'r')


# -를 경계로 데이터를 받아온다
num_lst = input().split('-')

for num in range(len(num_lst)):
    if '+' in num_lst[num]:
        temp = num_lst[num].split('+')
        temp_sum = 0
        for t in temp:
            temp_sum += int(t)
        num_lst[num] = temp_sum

ans = int(num_lst[0])
for num in range(1, len(num_lst)):

    ans -= int(num_lst[num])

print(ans)