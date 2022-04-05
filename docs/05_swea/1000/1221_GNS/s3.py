import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    numbertoa = ['ZRO', 'ONE','TWO','THR','FOR','FIV','SIX', 'SVN','EGT','NIN']

    numbers = list(input().split())

    ans = []
    for i in range(0, 10):
        for num in numbers:
            if numbertoa[i] == num:
                ans.append(num)

    print(ans)