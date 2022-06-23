# 3046_R2_문제풀이
# 2022-03-31

import sys
sys.stdin = open('input.txt', 'r')

R1, S = map(int, input().split())

ans = 2 * S - R1
print(ans)