import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
seat_lst = input()
i, cnt = 0, 1
while i < N:
    if seat_lst[i] == 'S':
        i += 1
        cnt += 1
    elif seat_lst[i] == 'L':
        i += 2
        cnt += 1
ans = 0
if N > cnt : ans = cnt
else : ans = N
print(ans)