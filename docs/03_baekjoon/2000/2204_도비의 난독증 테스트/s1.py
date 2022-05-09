# 2204 도비의 난독증 테스트_문제풀이
# 2022-05-09

import sys
sys.stdin = open('input.txt', 'r')


while True:
    N = int(input())
    # 종료조건
    if N == 0:
        break
    # 입력
    word = [input() for _ in range(N)]
    # 정렬
    word.sort(key=str.lower)
    # 출력
    print(word[0])