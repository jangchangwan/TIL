import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))
    cnt = 0
    for i in range(1, len(N_lst)-1):
        temp = N_lst[i-1:i+2]
        if temp[1] != max(temp) and temp[1] != min(temp):
            cnt += 1

    print(f'#{tc} {cnt}')