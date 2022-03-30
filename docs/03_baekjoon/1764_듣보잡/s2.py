# 1764_듣보잡_문제풀이
# 2022-03-30
# 시간초과
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
temp_lst = []
ans_lst = []

for _ in range(N+M):
    temp = input()
    if temp in temp_lst:
        ans_lst.append(temp)
    else:
        temp_lst.append(temp)

print(len(ans_lst))
ans_lst.sort()
for ans in ans_lst:
    print(ans)