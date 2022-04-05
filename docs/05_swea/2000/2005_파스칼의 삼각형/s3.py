# 2005_파스칼의-삼각형 풀이
# 2022-02-21
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [1]

    print('#{}'.format(tc))
    for i in range(N-1):
        stack = [0] + pascal + [0]
        pascal = []

        num_A = stack.pop()

        while stack != 0:
            num_B = stack.pop()
            pascal.append(num_A + num_B)
            num_A = num_B

    print(*pascal)