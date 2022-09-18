# 1453_피시방 알바
# 2022-09-05

N = int(input())
arr = list(map(int, input().split()))

count = [0] * 101

cnt = 0
for i in arr:
    if count[i]:
        cnt += 1
    else:
        count[i] = 1

print(cnt)