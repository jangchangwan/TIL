import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for t in range(N):
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))

    len_A = A_lst[0]
    len_B = B_lst[0]
    A_lst = A_lst[1:]
    B_lst = B_lst[1:]

    if len_A > len_B:
        max_len = len_A
        min_len = len_B
    else:
        max_len = len_B
        min_len = len_A

    A_lst.sort()
    B_lst.sort()

    A_lst = A_lst[::-1]
    B_lst = B_lst[::-1]

    for i in range(min_len):
        if A_lst[i] == B_lst[i]:
            if i == (min_len-1):
                if min_len == max_len:
                    print('D')
                    break
                else:
                    if max_len == len_A:
                        print('A')
                        break
                    else:
                        print('B')
                        break
            else:
                continue
        elif A_lst[i] > B_lst[i]:
            print('A')
            break
        else:
            print('B')
            break
