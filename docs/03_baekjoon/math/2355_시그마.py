def sigma (start, end):
    if start > end:
        start, end = end, start
    return end * ( end + 1 ) // 2 - start * ( start - 1 ) // 2 

A, B = map(int, input().split())

print(sigma(A, B))