import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

man_lst = [0]*7
women_lst = [0]*7

for i in range(N):
    gender, grade = map(int, input().split())

    if gender == 1:
        man_lst[grade] += 1
    else:
        women_lst[grade] += 1

cnt = 0
for j in range(1, 7):
    cnt += man_lst[j] // K
    if man_lst[j] % K != 0:
        cnt += 1

    cnt += women_lst[j] // K
    if women_lst[j] % K != 0:
        cnt += 1

print(cnt)