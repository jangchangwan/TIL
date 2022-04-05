# 1216_회문2_문제풀이
# 2022-02-17
import sys
sys.stdin = open('input.txt', 'r')

T = 10

for t in range(T):
    case_num = int(input())
    arr = [input() for _ in range(100)]
    # 전치 행렬
    trans_arr = [''.join(x) for x in zip(*arr)]
    # 행렬 크기
    N = 100
    # 최대 회문 길이
    max_C = 1

    # 큰것부터 찾기위해 역순으로
    for k in range(2, 100):
        for i in range(N):
            for j in range(N-k+1):
                # 가로로 글자받기
                arr_row = arr[i]
                row_list = arr_row[j:j + k]
                # 세로로 글자 받기
                arr_col = trans_arr[i]
                col_list = arr_col[j:j + k]
                # 슬라이싱으로  비교
                if row_list == row_list[::-1] or col_list == col_list[::-1]:
                    if k > max_C:
                        max_C = k
                        # 제일큰값이므로 바로 빠져나온다.
                        break

    ans = max_C
    print('#{} {}'.format(case_num, ans))