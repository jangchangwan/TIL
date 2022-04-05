import sys

sys.stdin = open('input.txt', 'r')

T = 10

for t in range(10):
    N = int(input())
    # 인덱스 에러 방지와 1부터 시작하는 인덱스를 만들기 위해 0으로 테두리를 만듬
    arr = [[0]*102] + [[0]+list(map(int, input().split()))+[0] for _ in range(100)] + [[0]*102]
    # 도착지는 값이 2이므로 2인 col값을 찾는다.
    for j in range(102):
        if arr[100][j] == 2:
            c = j
    # 출발위치
    row = 100
    col = c

    k = 0
    # 좌우로 왔다갔다 반복하는 것을 막기위해
    cnt = 0
    dr = [-1, 0, 0]
    dc = [0, 1, -1]

    while row > 1:
        row += dr[k]
        col += dc[k]
        # 오른쪽
        if arr[row][col-1] == 0 and arr[row][col+1] == 1:
            if cnt % 2 == 1:
                k = 0
            else:
                k = 1
            cnt += 1
        # 왼쪽
        elif arr[row][col-1] == 1 and arr[row][col+1] == 0:
            if cnt % 2 == 1:
                k = 0
            else:
                k = 2
            cnt += 1
        # 아닐경우 이전 동작을 반복한다
        else:
            continue

    print('#{} {}'.format(N, col-1))