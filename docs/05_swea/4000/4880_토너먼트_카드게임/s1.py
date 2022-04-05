import sys
sys.stdin = open('input.txt', 'r')


def partition(arr, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end

T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    stu_lst = [i for i in range(1, N+1)]
    stu_stack = []
    stack = [(num_lst[0], num_lst[1])]
    i = 0
    while stack:
        num1, num2 = stack.pop()
        print(num1, num2)
        i += 2
    ans = 0
    print('#{} {}'.format(t, ans))