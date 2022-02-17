# 부분문자열_문제풀이
# 2022-02-17
import sys
sys.stdin = open('input.txt', 'r')

text = input()
word = input()

if word in text:
    print(1)
else:
    print(0)