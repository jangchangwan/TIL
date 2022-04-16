# 1173_운동_문제풀이
# 2022-04-15

import sys
sys.stdin = open('input.txt', 'r')


N, min_bpm, max_bpm, up, down = map(int, input().split())

cnt = 0
up_cnt = 0
start = min_bpm

if (max_bpm - min_bpm) < up:
    print(-1)
    exit()

while up_cnt < N :
    if start + up <= max_bpm:
        up_cnt += 1
        start += up
    elif start + up > max_bpm:
        if start - down >= min_bpm:
            start -= down
        else:
            start = min_bpm
    cnt += 1

print(cnt)

