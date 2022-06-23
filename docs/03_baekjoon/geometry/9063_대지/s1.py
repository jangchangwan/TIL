# 9063_대지
# 2022-06-15


N = int(input())

min_x, min_y = 10000, 10000
max_x, max_y = -10000, -10000

for _ in range(N):
    x, y = map(int, input().split())
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y


res = (max_y - min_y) * (max_x - min_x)
print(res)