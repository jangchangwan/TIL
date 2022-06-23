# 가로, 세로
w, h = map(int, input().split())
# 좌표
x, y = map(int, input().split())
# 시간
t = int(input())

x_t = t % (2 * w)
y_t = t % (2 * h)

x_add = 1
y_add = 1

while x_t > 0:
    if x == w or x == 0:
        x_add = -x_add
    x += x_add
    x_t -= 1
while y_t > 0:
    if y == 0 or y == h:
        y_add = -y_add
    y += y_add
    y_t -= 1

print(x, y)