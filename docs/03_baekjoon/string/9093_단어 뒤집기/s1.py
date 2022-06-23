# 9093 단어 뒤집기
# 2022-06-21

T = int(input())

for tc in range(T):
    word = list(input().split())
    ans = []
    for w in word:
        ans.append(w[::-1])

    print(*ans)