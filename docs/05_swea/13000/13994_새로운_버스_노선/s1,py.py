import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for c in range(1, T+1):
    N = int(input())
    d = [0]*1001
    for n in range(N):
        t,s,e = map(int, input().split())
        d[s] += 1
        d[e] += 1
        if t == 1:
            for i in range(s+1,e):d[i] += 1
        elif t == 2:
            for i in range(s+2,e,2):d[i] += 1
        else:
            if s % 2:
                for i in range(s+1, e):
                    if i % 3 == 0 and i % 10 != 0:d[i] += 1
            else:
                for i in range(s+1, e):
                    if i % 4 == 0:d[i] += 1
    r = 0
    for i in range(1, 1001):
        if d[i] > r:r = d[i]
    print('#{} {}'.format(c, r))
