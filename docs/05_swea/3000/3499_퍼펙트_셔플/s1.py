import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    text_lst = list(map(str, input().split()))

    even_lst = list()
    odd_lst = list()
    if N % 2:
        mid = (N // 2) + 1
    else:
        mid = (N // 2)

    a_lst = text_lst[:mid]
    b_lst = text_lst[mid:]

    res = ''
    for i in range(len(b_lst)):
        res += a_lst[i] + ' ' + b_lst[i] + ' '

    if N % 2:
        res += a_lst[mid-1]
    else:
        res = res[:len(res)-1]
    print('#{} {}'.format(tc, res))