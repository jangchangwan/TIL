# 4865_글자수_문제풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    word = input()
    text = input()
    max_cnt = 0
    # 중복제거
    new_word = ''
    for k in word:
        if k not in new_word:
            new_word += k

    for i in new_word:
        cnt = 0
        for j in text:
            if i == j:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    ans = max_cnt
    print('#{} {}'.format(t, ans))