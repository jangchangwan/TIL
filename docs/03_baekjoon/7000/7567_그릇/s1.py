# 7567_그릇
# 2022-06-21

word = input()

ans = 10
for i in range(1, len(word)):
    if word[i] == word[i-1]:
        ans += 5
    else:
        ans += 10

print(ans)