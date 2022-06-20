# 11656 접미사 배열
# 2022-06-21

word = input()

answer = list()

for i in range(len(word)):
    answer.append(word[i:len(word)])

answer.sort()
for ans in answer:
    print(ans)