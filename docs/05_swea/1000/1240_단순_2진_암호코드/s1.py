# 1240_단순_2진_암호코드_문제풀이
# 2022-03-23
import sys
sys.stdin = open('input.txt', 'r')
# 각 번호의 코드
# 뒤에는 무조건 1로 시작
# 뒤에서부터 보게될 경우 암호코드가 시작하는 부분을 알 수 있음
num_arr = [
        [0, 0, 0, 1, 1, 0, 1],  # 0
        [0, 0, 1, 1, 0, 0, 1],  # 1
        [0, 0, 1, 0, 0, 1, 1],  # 2
        [0, 1, 1, 1, 1, 0, 1],  # 3
        [0, 1, 0, 0, 0, 1, 1],  # 4
        [0, 1, 1, 0, 0, 0, 1],  # 5
        [0, 1, 0, 1, 1, 1, 1],  # 6
        [0, 1, 1, 1, 0, 1, 1],  # 7
        [0, 1, 1, 0, 1, 1, 1],  # 8
        [0, 0, 0, 1, 0, 1, 1]   # 9
    ]

# 끝 찾기
def start_dir():
    for i in range(N - 1, 0, -1):
        for j in range(M - 1, 0, -1):
            if base_arr[i][j] == 1:
                return [i, j]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 가로, 세로
    base_arr = [list(map(int, input())) for _ in range(N)]  # 암호코드

    # 끝 찾기
    start_r, start_c = start_dir()
    # 암호코드 만들기
    pass_code = base_arr[start_r][start_c-55:start_c+1]

    temp = []
    # 각자리의 번호 뽑기
    for i in range(0, 56, 7):
        num = pass_code[i:i + 7]
        for j in range(10):
            if num == num_arr[j]:
                temp.append(j)
    # 정상적인 암호코드인지 확인
    temp_sum = 0
    for i in range(8):
        if i % 2:
            temp_sum += temp[i]
        else:
            temp_sum += (temp[i]*3)
    if temp_sum % 10:
        ans = 0
    else:
        ans = sum(temp)
    print('#{} {}'.format(tc, ans))

