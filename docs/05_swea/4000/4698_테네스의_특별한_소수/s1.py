import sys
sys.stdin = open('input.txt', 'r')


def sosu(num):
    if num <= 1:
        return 0
    elif num == 2:
        return num
    for i in range(2,num):
        if num % i == 0:
            return 0
    return num


T = int(input())

for tc in range(1, T+1):
    K, start, end = map(int, input().split())

    num_lst = []

    for num in range(start, end+1):
        number = num
        while number > 0:
            if number % 10 == K:
                num_lst.append(num)
            number //= 10
    for num in num_lst:
        number = sosu(num)
        if number == 0:
            num_lst.remove(num)

    print(num_lst)



