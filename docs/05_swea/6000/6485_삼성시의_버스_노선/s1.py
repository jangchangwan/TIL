# 6485_삼성시의_버스_노선_문제풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    bus_station = [0] * 5001
    for n in range(N):
        start, end = map(int, input().split())
        for i in range(start, end + 1):
            bus_station[i] += 1

    P = int(input())

    result = list()
    for j in range(1, P+1):
        result.append(bus_station[int(input())])

    print('#{}'.format(t), end=' ')
    for z in result:
        print(z, end=' ')
    print()