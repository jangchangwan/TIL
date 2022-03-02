import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    A %= 10
    num_lst = [A]
    for i in range(B-1):
        num = (num_lst[i] * A) % 10
        if num in num_lst:
            break
        num_lst.append(num)
    ans = num_lst[(B % len(num_lst)) - 1]
    if ans == 0:
        print(10)
    else:
        print(ans)