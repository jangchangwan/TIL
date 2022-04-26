# 1755_숫자놀이_문제풀이
# 2022-04-26

import sys
sys.stdin = open('input.txt', 'r')


tans_string = {
    '1': 'one', '2': 'two', '3': 'three',
    '4': 'four', '5': 'five', '6': 'six',
    '7': 'seven', '8': 'eight', '9': 'nine',
    '0': 'zero'
  }

tans_int = {
    'one': '1', 'two': '2', 'three': '3',
    'four': '4', 'five': '5', 'six': '6',
    'seven': '7', 'eight': '8', 'nine': '9',
    'zero': '0'
  }

start, end = map(int, input().split())

n_lst = []
for i in range(start, end+1):
    n_lst.append(str(i))

tans_lst = []
for n in n_lst:
    temp = []
    for i in n:
        temp.append(tans_string[i])
    tans_lst.append(temp)

tans_lst.sort()
ans_lst = []
for n in tans_lst:
    temp = ''
    for i in n:
        temp += tans_int[i]
    ans_lst.append(temp)

cnt = 0
for ans in ans_lst:
    cnt += 1
    if cnt == 10:
        cnt = 0
        print(ans)
    else:
        print(ans, end=' ')