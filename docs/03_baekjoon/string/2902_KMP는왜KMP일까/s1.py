# 2902 KMP는 왜 KMP일까?
# 2022-06-21

word = list(input().split('-'))
answer = ''
for w in word:
    answer += w[0]
print(answer)