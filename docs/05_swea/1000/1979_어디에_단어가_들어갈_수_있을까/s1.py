import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # input data 받아오기
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 가로 탐색
    for i in range(N):
        cnt_row = 0

        for j in range(N):
            # 1일경우 카운트 1씩증가
            if arr[i][j] == 1:
                cnt_row += 1
            # 바뀔경우 1의 개수를 확인하고 맞으면 포함
            else:
                if cnt_row == K:
                    result += 1
                cnt_row = 0
        # 끝에 도달했을때
        if cnt_row == K:
            result += 1
    # print('row: ',result )
    # 세로 계산하는거
    for i in range(N):
        cnt_col = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt_col += 1
            else:
                if cnt_col == K:
                    result += 1
                cnt_col = 0
        if cnt_col == K:
            result += 1
    # print('row+col: ', result)
    print('#{} {}'.format(t, result))
