# 1271_임청난 부자2 문제풀이
# 2022-04-20


import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())

print(N // M)
print(N % M)