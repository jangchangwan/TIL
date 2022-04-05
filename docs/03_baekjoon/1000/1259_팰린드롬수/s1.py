import sys
sys.stdin = open('input.txt', 'r')

while 1:
    num = input()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')