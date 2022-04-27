# 1931_회의실 배정_문제풀이
# 2022-04-21

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

arr = sorted(arr, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
arr = sorted(arr, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in arr:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)