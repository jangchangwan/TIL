# 10773_제로_문제풀이
# 2022-02-23
import sys
sys.stdin = open('input.txt', 'r')

stack = []
N = int(sys.stdin.readline())

for n in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
sum_num = 0
for s in stack:
    sum_num += s
print(sum_num)