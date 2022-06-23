# 19948_음유시인 영재
# 2022-06-21

text = list(input().split())

space = int(input())
alphabet = list(map(int, input().split()))
# 스페이스가 부족한 경우
if len(text)-1 > space:
    print(-1)
else:
    # 타이틀 구하기
    title = ''
    for t in text:
        title += t[0].upper()
    text.append(title)
    for t in text:
        for i in range(len(t)-1):
            if t[i] == t[i+1]:
                continue
            else:
                if alphabet[ord(t[i].lower())-97]:
                    alphabet[ord(t[i].lower())-97] -= 1
                else:
                    print(-1)
                    exit()
    else:
        print(title)