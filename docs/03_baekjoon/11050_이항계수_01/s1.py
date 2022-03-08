N, K = map(int, input().split())

def fn(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fn(n-1)


ans = fn(N) / (fn(K) * fn(N-K))
print(int(ans))