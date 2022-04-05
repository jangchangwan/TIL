# 9184_신나는 함수 실행_문제풀이
# 2022-03-31
import sys
sys.stdin = open('input.txt', 'r')


while True:
    a, b, c = map(int, input().split())
    # 종료조건
    if a == -1 and b == -1 and c == -1:
        break

    print(a,b,c)