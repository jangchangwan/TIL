# 4864_문자열_비교_문제풀이
# 2022-02-17
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # 찾을 단어
    word = input()
    # 검색할 텍스트
    text = input()
    ans = 0
    for i in range(len(text)-len(word)+1):
        if text[i:i+len(word)] == word:
            ans = 1
            break
        ans = 0

    print('#{} {}'.format(t, ans))
