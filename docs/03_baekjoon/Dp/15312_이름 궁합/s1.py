# 15312_이름 궁합_문제풀이
# 2022-05-12

import sys
sys.stdin = open('input.txt', 'r')

data = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]


first_name = input()
second_name = input()
couple = []
for i in range(len(first_name)):
    couple.append(data[ord(first_name[i])-65])
    couple.append(data[ord(second_name[i])-65])

# print(couple)
while True:
    temp = []
    for i in range(len(couple)-1):
        temp.append((couple[i] + couple[i+1]) % 10)


    couple = temp
    # print(couple)
    if len(couple) == 2:
        break

print(str(couple[0])+str(couple[1]))