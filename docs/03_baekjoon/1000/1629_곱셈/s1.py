# 1629_곱셈_문제풀이
# 2022-04-13


'''
지수는 분배가 가능하다
10 ^ 11 = 10 ^ 2   * 10 ^ 2 * 10^ 7 이런식으로 줄여서 나눠서 계산하면 시간이줄어들거같다.
'''
import sys
sys.stdin = open('input.txt', 'r')


def my_distribution(A, n):
    if n == 1:
        return  A % C
    else:
        temp = my_distribution(A, n//2)
        if n % 2 == 0:
            return (temp * temp) % C
        else:
            return (temp * temp * A) % C


A, N, C = map(int, input().split())

print(my_distribution(A, N))
