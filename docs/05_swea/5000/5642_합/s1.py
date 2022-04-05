import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))
    
    ans = 0
    print('#{} {}'.format(tc, ans))