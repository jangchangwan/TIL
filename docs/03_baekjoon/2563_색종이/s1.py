import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

arr = [[0]*100 for _ in range(100)]
ans = 0
for t in range(T):
    col, row = map(int, input().split())

    for i in range(row, row+10):
        for j in range(col, col+10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                ans += 1
print(ans)