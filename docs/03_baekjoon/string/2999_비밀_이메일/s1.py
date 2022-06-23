import sys
sys.stdin = open('input.txt', 'r')

text = input()
N = len(text)
row = col = 0
for i in range(1, int(N**0.5)+1):
    for j in range(i, N+1):
        if i * j == N:
            row, col = i, j
k = 0
arr = [[0] * col for _ in range(row)]
for j in range(col):
    for i in range(row):
        arr[i][j] = text[k]
        k += 1


for i in range(row):
    for j in range(col):
        print(arr[i][j], end='')
