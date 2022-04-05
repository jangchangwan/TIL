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
    i = 0
    # 테스트 케이스 만큼 시행
    while i < tc:
        # 동일할 경우
        if text[i:i+len(word)] == word:
            cnt += 1
            i += len(word)
            continue
        i += 1
    ans = cnt
    print('#{} {}'.format(N, ans))