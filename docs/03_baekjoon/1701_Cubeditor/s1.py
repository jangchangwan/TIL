# Cubeditor_문제풀이
# 2022-02-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    text = input()
    N = len(text)
    max_num = 0
    for k in range(N-1, 1, -1):
        if max_num > k:
            break
        for i in range(0, N-k+1):
            for j in range(1, N-k+1):
                if text[i:i+k] == text[i+j:i+j+k]:
                    max_num = k
                    break
    print(max_num)