import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = list(input())

    max_num = 0
    min_num = 999999999
    for i in range(len(N)):
        for j in range(i, len(N)):
            new_N = N[:]
            new_N[i], new_N[j] = new_N[j], new_N[i]
            number = int(''.join(new_N))
            if number > max_num and (new_N[0] != '0'):
                max_num = number
            if (number < min_num) and (new_N[0] != '0'):
                min_num = number
    if N[0] == '0':
        min_num = 0

    print('#{} {} {}'.format(tc, min_num, max_num))