# 25306_연속 XOR
# 2022-06-25
# 수학 / 비트마스킹

def computeXOR(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0

def xorSum(a,b):
    return computeXOR(a-1) ^ computeXOR(b)

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    print(xorSum(A, B))