# import sys
# input = sys.stdin.readline

N, B = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]

# 계산
def calculate(U, V):
    n = len(U)
    temp = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            temp[row][col] = e % 1000

    return temp

# 분할
def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    temp = square(A, B//2)
    if B % 2:
        return calculate(calculate(temp, temp), A)
    else:
        return calculate(temp, temp)

result = square(arr, B)
for r in result:
    print(*r)