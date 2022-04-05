# 3143_가장_빠른_문자열_타이밍_문제풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    text, word = input().split()
    # 전체길이
    cnt = len(text)

    i = 0
    try_cnt = 0
    while i < len(text)-len(word)+1:
        if text[i: i+len(word)] == word:
            # 같을경우 단어 갯수만큼 차감
            cnt -= len(word)
            # 건너뛰기
            i += len(word)
            # 트라이횟수 증감
            try_cnt += 1
        else:
            i += 1
    ans = cnt + try_cnt
    print('#{} {}'.format(t, ans))