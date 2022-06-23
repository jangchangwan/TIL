import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

arr = [[0]*1001 for _ in range(1001)]

max_num = [0, 0]
min_num = [1001, 1001]

for ta in range(1, T+1):

    x1, y1, w, h = map(int, input().split())

    for i in range(x1, x1+w):
        arr[i][y1:y1+h] = [ta]*h

    if x1 < min_num[0]:
        min_num[0] = x1
    if y1 < min_num[1]:
        min_num[1] = y1
    if x1+w > max_num[0]:
        max_num[0] = x1+w
    if y1+h > max_num[1]:
        max_num[1] = y1+h

for tb in range(1, T+1):
    cnt = 0
    for k in range(min_num[0], max_num[0]):
        for h in range(min_num[1], max_num[1]):
            if arr[k][h] == tb:
                cnt += 1
    print(cnt)
