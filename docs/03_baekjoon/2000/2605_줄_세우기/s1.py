import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
stu_lst = list()
for n in range(N):
    # 학번 맞추기 위해서
    stu_lst += [n+1]

    for t in range(nums[n]):
        stu_lst[n-t], stu_lst[n-t-1] = stu_lst[n-t-1], stu_lst[n-t]

print(*stu_lst)