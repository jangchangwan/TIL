# 10768_특별한 날_문제풀이
# 2022-05-15

import sys
sys.stdin = open('input.txt', 'r')

Month = int(input())
day = int(input())

if Month < 2:
    print('Before')
elif Month > 2:
    print('After')
else:
    if day < 18:
        print('Before')
    elif day > 18:
        print('After')
    else:
        print('Special')