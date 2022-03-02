import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
result = list()
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    N_lst = [0]*101
    ans = min(B, D) - max(A, C)
    if ans < 0:
        ans = 0
    result.append('#{} {}'.format(tc, ans))
print('\n'.join(result))