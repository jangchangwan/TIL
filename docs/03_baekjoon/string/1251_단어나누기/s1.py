# 1251_단어나누기_문제풀이
# 2022-05-01

import sys
sys.stdin = open('input.txt', 'r')

word = input()

temp = []
for i in range(1, len(word)-1):
    for j in range(i + 1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        temp.append(a + b + c)
temp.sort()
print(temp[0])