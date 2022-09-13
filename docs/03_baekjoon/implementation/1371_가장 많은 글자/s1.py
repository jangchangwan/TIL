# 1371_가장많은 글자


import sys

words = sys.stdin.read().replace('\n', '').replace(' ', '')



li = [0] * 26
for chr in words:
    if chr.islower():
        li[ord(chr) - 97] += 1
for i in range(26):
    if li[i] == max(li):
        print(chr(97 + i), end='')