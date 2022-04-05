import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    hour_1, min_1, hour_2, min_2 = map(int, input().split())

    new_hour = hour_1 + hour_2
    new_min = min_1 + min_2

    if new_min >= 60:
        new_min -= 60
        new_hour += 1

    if new_hour > 12:
        new_hour -= 12

    print('#{} {} {}'.format(tc, new_hour, new_min))