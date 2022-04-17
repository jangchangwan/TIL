# 1264_모음의개수_문제풀이
# 2022-04-17

import sys
sys.stdin = open('input.txt', 'r')

# 모음 리스트를 만들고 그리스트안에 있을경우 count를 1씩 늘려준다
# 카운터를 출력

vowel_lst = ['a', 'e', 'i', 'o', 'u']

while True:
    data = input()
    if data == '#':
        break
    data = data.lower()
    cnt = 0
    for d in data:

        if d in vowel_lst:
            cnt += 1

    print(cnt)
