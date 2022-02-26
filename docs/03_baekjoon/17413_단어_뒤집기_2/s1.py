import sys
sys.stdin = open('input.txt', 'r')

text = list(input())

res = ''
temp = ''
# 반복한다
t = 0
while t < len(text):
    if text[t] == '<':
        res += temp[::-1]
        temp = ''
        res += text[t]
        t += 1
        while True:
            if text[t] == '>':
                res += text[t]
                t += 1
                break
            res += text[t]
            t += 1

    elif text[t] == ' ':
        res += temp[::-1]
        res += text[t]
        temp = ''
        t += 1
    else:
        temp += text[t]
        t += 1
res += temp[::-1]
print(res)