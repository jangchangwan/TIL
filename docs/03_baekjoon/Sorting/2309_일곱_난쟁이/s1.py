import sys
sys.stdin = open('input.txt', 'r')

T = 9

child_list = list()
sum_child = 0

for i in range(9):
    child = int(input())
    child_list.append(child)
    sum_child += child


for i in range(9):
    for j in range(i+1, 9):
        if sum_child - child_list[i] - child_list[j] == 100:
            # 바로 remove 할경우 인덱스 배치가 달라진다
            num_1 = child_list[i]
            num_2 = child_list[j]
            child_list.remove(num_1)
            child_list.remove(num_2)
            child_list.sort()
            break
    if len(child_list) < 9:
        break

for i in child_list:
    print(i)