import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ans = 'No'
    for i in range(1,10):
        for j in range(1,10):
            if N == (i * j):
                ans = 'Yes'
    print('#{} {}'.format(tc, ans))