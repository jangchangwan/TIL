import sys
sys.stdin = open('input.txt', 'r')

num_lst = list()
score = 0
for i in range(10):
    num_lst.append(int(input()))
for j in num_lst:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)