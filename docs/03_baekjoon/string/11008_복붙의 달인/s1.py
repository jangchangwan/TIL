# 11008_복붙의 달인
# 2022-06-22

T = int(input())

for tc in range(T):
    word, repeat = input().split()
    cnt = 0
    L = len(repeat)
    i = 0
    while i < len(word):
        if word[i:i+L] == repeat:
            cnt += 1
            i += L
        else:
            cnt += 1
            i += 1
    print(cnt)