import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
text = input()
ans = 0

for n in range(len(text)):
    temp = (ord(text[n])-96) * (31**n)
    ans += temp
print(ans % 1234567891)