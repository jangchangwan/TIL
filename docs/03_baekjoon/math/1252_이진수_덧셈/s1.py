
# 1252_이진수_덧셈_문제풀이
# 2022-04-17

import sys
sys.stdin = open('input.txt', 'r')

# 받아올때 2진수로 받아와서 더해준다


a, b = map(str, input().split())

print(bin(int(a, 2) + int(b, 2))[2:])
