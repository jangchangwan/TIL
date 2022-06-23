# 25206_너의 평점은_문제풀이
# 2022-05-26

import sys
sys.stdin =open('input.txt', 'r')

score_dic = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0
}


total = 0
total_credit = 0
for _ in range(20):
    name, credit, grade = map(str, input().split())
    if grade in score_dic.keys():
        total += float(credit) * score_dic[grade]
    if grade == 'P':
        continue
    total_credit += float(credit)

print(total/total_credit)