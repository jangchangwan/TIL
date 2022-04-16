# 1212_8진수_2진수_문제풀이
# 2022-04-16

import sys
sys.stdin = open('input.txt', 'r')

num = int(input(), 8)

print(bin(num)[2:])