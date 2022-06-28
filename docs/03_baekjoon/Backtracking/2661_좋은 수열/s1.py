# 2661_좋은 수열
# 2022-06-27
# 백트래킹

def Back_tracking(n, arr):
    for i in range(1, (n//2)+1):
        if arr[-i:] == arr[-(i*2):-i]:
            return -1

    if n == N:
        print(arr)
        exit()
    for i in '123':
        arr += i
        if Back_tracking(n+1, arr) == 0:
            return 0
        arr = arr[:-1]


N = int(input())
Back_tracking(1, '1')
