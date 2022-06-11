# 19564_반복_문제풀이
# 2022-06-11

word = input()

cnt = 1
max_val = 0
for i in range(1, len(word)):
    if word[i] <= word[i-1]:
        cnt += 1
print(cnt)