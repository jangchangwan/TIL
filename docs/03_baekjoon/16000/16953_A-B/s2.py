# 16953_A->B_문제풀이
# 2022-04-13

import sys
sys.stdin = open('input.txt', 'r')

start, end = map(int, input().split())
cnt = 1

while True:
    if start == end:
        break

    elif (end % 2 != 0 and end % 10 != 1) or (end < start):
        cnt = -1
        break


    else:
        if end % 10 == 1:
            end //= 10
            cnt += 1
        else:
            end //= 2
            cnt += 1


print(cnt)