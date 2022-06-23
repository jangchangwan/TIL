# 2609_최대공약수와 최소공배수_문제풀이
# 2022-04-05
import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())


# 최대공약수
ans_1 = 0
if N > M:
    temp = M
else:
    temp = N
for i in range(temp, 0, -1):
    if N % i == 0 and M % i == 0:
        ans_1 = i
        break

# 최소공배수
n = 1
m = 1

while True:
    temp_n = N * n
    temp_m = M * m
    while temp_n > temp_m:
        temp_m = M * m
        m += 1

    if temp_n == temp_m:
        ans_2 = temp_n
        break
    n += 1

print(ans_1)
print(ans_2)