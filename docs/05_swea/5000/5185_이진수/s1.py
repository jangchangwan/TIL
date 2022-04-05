# 5185_이진수 문제풀이
# 2022-03-24

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
# 각 번호별 2진수 값 넣기
data = {
    '0': '0000',    '1': '0001',    '2': '0010',    '3': '0011',
    '4': '0100',    '5': '0101',    '6': '0110',    '7': '0111',
    '8': '1000',    '9': '1001',    'A': '1010',    'B': '1011',
    'C': '1100',    'D': '1101',    'E': '1110',    'F': '1111',
}

for tc in range(1, T+1):
    # 입력
    N, N_lst = map(str, input().split())
    # 문자열에 집어넣기
    ans = ''
    for i in range(int(N)):
        ans += data[N_lst[i]]
    # 출력
    print('#{} {}'.format(tc, ans))