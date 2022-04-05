# 1970_쉬운_거스름돈_문제풀이
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    money = int(input())
    ans_lst = [0] * 8

    if money // 50000 != 0:
        ans_lst[0] = money // 50000
        money %= 50000
    if money // 10000 != 0:
        ans_lst[1] = money // 10000
        money %= 10000
    if money // 5000 != 0:
        ans_lst[2] = money // 5000
        money %= 5000
    if money // 1000 != 0:
        ans_lst[3] = money // 1000
        money %= 1000
    if money // 500 != 0:
        ans_lst[4] = money // 500
        money %= 500
    if money // 100 != 0:
        ans_lst[5] = money // 100
        money %= 100
    if money // 50 != 0:
        ans_lst[6] = money // 50
        money %= 50
    if money // 10 != 0:
        ans_lst[7] = money // 10
        money %= 10

    print('#{}'.format(tc))
    print(*ans_lst)