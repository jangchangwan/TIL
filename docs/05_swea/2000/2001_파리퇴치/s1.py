import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for i in range(1, T+1):
    size_number = list(map(int, input().split()))
    numbers_list = list()
    for j in range(size_number[0]):
        numbers_list.append(list(map(int, input().split())))
    max_number = 0
    for z in range(size_number[0]-size_number[1]+1):
        # max_number 구하기
        new_number = 0
        for w in range(z, size_number[1]+z):
            for h in range(z, size_number[1]+z):
                new_number += numbers_list[w][h]
        # 값을 구하면
        if new_number > max_number:
            max_number = new_number
    print('#{} {}'.format(i, max_number))
