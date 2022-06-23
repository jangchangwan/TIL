import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cnt = 0
for i in range(1, int(N**0.5)+1):
    cnt += (N // i) - (i - 1)
print(cnt)