import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    N_lst = []
    for n in range(N):
        A, B, C = map(int, input().split())
        ave = (A * 0.35 + B * 0.45 + C * 0.2)
        N_lst.append(ave)

    Sort_lst = N_lst[:]
    Sort_lst.sort(reverse=True)

    cnt = 0
    ans = 0
    for s in Sort_lst:
        if s == N_lst[K-1]:
           ans = cnt
        cnt += 1
    score_lst = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    temp = ans // (N // 10)

    print('#{} {}'.format(tc, score_lst[temp]))