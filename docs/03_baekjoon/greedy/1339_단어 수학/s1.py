# 1339_단어 수학
# 2022-06-27
# 그리드 알고리즘

T = int(input())
words = [input() for _ in range(T)]

alpha_dict = {}

for word in words:
    weight = len(word) - 1
    for char in word:
        if char in alpha_dict:
            alpha_dict[char] += 10 ** weight
        else:
            alpha_dict[char] = 10 ** weight
        weight -= 1

alpha_dict = sorted(alpha_dict.values(), reverse=True)

answer = 0
num = 9

for value in alpha_dict:
    answer += value * num
    num -= 1

print(answer)