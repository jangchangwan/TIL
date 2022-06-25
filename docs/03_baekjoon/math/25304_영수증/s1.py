# 25304_영수증
# 2022-06-25
# 수학
answer = int(input())

N = int(input())

temp = 0
for _ in range(N):
    cost, cnt = map(int, input().split())
    temp += cost * cnt

if answer == temp:
    print('Yes')
else:
    print('No')