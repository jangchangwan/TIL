
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
n, m = N, M
while m != 0:
    n = n % m
    n, m = m, n
# gcd
print(n)
#lcm
print(N*M//n)

