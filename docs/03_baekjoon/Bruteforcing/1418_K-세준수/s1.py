# 1418_K-세준수
# 2022-06-28
# 브루트포스 + 에라토스테네스의 체

N = int(input())
K = int(input())

max_nums = [0 for i in range(N+1)]
for i in range(2, N+1):
    if max_nums[i] == 0:
        for j in range(i, N+1, i):
            if j % i == 0:
                max_nums[j] = max(max_nums[j], i)

answer = 0
for num in max_nums:
    if num <= K:
        answer += 1
print(answer - 1)