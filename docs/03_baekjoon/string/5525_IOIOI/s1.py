# 5525_IOIOI
# 2022-07-11

N = int(input())
M = int(input())
word = input()

answer = 0
cnt = 0
i = 1

while i < M - 1:
    if word[i-1] == "I" and word[i] == "O" and word[i+1] == "I":
        cnt += 1
        if cnt == N:
            cnt -= 1
            answer += 1
        i += 1
    else:
        cnt = 0
    i += 1

print(answer)