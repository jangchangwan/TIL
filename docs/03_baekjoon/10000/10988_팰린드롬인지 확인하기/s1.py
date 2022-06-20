# 10988_팰린드롬인지 확인하기
# 2022-06-21

word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)