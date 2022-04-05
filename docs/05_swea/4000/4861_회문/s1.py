# 4861_회문_문제풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # 데이터 받아오기
    N, C = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-C+1):
            # 가로로 글자받기
            row_list = arr[i][j:j+C]
            # 세로로 글자 받기
            col_list = [arr[x][i] for x in range(j, j+C)]
            # 슬라이싱으로  비교
            if row_list == row_list[::-1]:
                ans = row_list
                break
            elif col_list == col_list[::-1]:
                ans = col_list
                break
    # 출력
    print('#{}'.format(t), end=' ')
    for k in ans:
        print(k,end='')
    print()

