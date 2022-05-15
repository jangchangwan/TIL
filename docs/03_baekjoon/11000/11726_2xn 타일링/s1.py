# 11726_2xn 타일링_문제풀이
# 2022-05-12

import sys
sys.stdin = open('input.txt', 'r')

'''

    1   2   3   4   5   6   7   8   9   10
    
T   1   2   3   5   8   13  21  34  55  89

f(n) = f(n-2) + f(n-1)
'''


N = int(input())
DP = [0, 1, 2]
for i in range(3, N+1):
    DP.append(DP[i - 1]+DP[i - 2])
print(DP[N] % 10007)