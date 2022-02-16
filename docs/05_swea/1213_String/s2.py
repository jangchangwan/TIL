import sys
sys.stdin = open('input.txt', 'r', encoding='UTF8')

T = 10

for t in range(T):
    N = input()
    word = input()
    text = input()
    # 시행횟수
    tc = len(text)-len(word)+1
    # 동일한 경우
    cnt = 0
    for i in range(tc):
        if text[i:i+len(word)] == word:
            cnt += 1
    ans = cnt
    print('#{} {}'.format(N, ans))