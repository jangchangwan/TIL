# 10808_알파벳 개수
# 2022-06-18

abc_lst = [0] * 26

word = input()

for w in word:
    abc_lst[ord(w)-97] += 1

print(*abc_lst)
