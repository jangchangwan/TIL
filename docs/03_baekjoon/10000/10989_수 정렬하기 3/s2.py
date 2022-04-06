# 10989_수 정렬하기 3 문제풀이
# 2022-04-06
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

check_num = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())

    check_num[num] = check_num[num] + 1

for i in range(1, 10001):
    if check_num[i] == 0:
        continue
    for j in range(check_num[i]):
        print(i)