# 11721_열 개씩 끊어 출력하기
# 2022-06-21

word = input()

for i in range(0, len(word), 10):
    print(word[i:i+10])