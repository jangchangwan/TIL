# 2163_초콜릿-자르기_문제풀이
# 2022-03-31
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
ans = (N-1) + (M-1) * N
print(ans)