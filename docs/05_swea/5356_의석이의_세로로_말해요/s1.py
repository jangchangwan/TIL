# 5356_의석이의_세로로_말해요_문제풀이
# 2022-02-17
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    arr = [list(input()) for i in range(5)]

    result = ''
    # 최대문자열 갯수
    for i in range(15):
        # 5문장
        for j in range(5):
            # 행 길이가 인덱스보다 클경우만 작동
            if len(arr[j]) > i:
                result += arr[j][i]
    ans = result
    print('#{} {}'.format(t, ans))



