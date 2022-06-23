# 2930_가위 바위 보_문제풀이
# 2022-04-29

import sys
sys.stdin = open('input.txt', 'r')

R = int(input())
me = input()
N = int(input())

save = [[0, 0, 0] for _ in range(R)]


ans = 0
max_ans = 0

for _ in range(N):
    friend = input()
    for idx, val in enumerate(friend):
        save[idx]['RSP'.index(val)] += 1

    for idx, val in enumerate(me):
        # 비겼을 경우
        if val == friend[idx]:
            ans += 1
        # 이겼을 경우
        elif (val, friend[idx]) in [('S', 'P'), ('P', 'R'), ('R', 'S')]:
            ans += 2

for val in save:
        max_ans += max(val[0] + val[1] * 2, val[1] + val[2] * 2, val[2] + val[0] * 2)

print(ans)
print(max_ans)