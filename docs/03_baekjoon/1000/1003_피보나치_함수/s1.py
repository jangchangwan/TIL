import sys
sys.stdin = open('input.txt', 'r')


def fibonacci(n):
    global data
    global cnt_data
    if n >= 2 and len(data) <= n:
        data.append(fibonacci(n-1)+fibonacci(n-2))
        cnt_data.append([cnt_data[n-1][0]+cnt_data[n-2][0], cnt_data[n-2][1] + cnt_data[n-1][1]])
    return cnt_data[n]


T = int(input())

data = [0, 1, 1, 2, 3]
cnt_data = [[1, 0], [0, 1], [1, 1], [1, 2], [2, 3]]
for tc in range(1, T+1):
    N = int(input())
    cnt = [0, 0]
    ans = fibonacci(N)
    print(*ans)