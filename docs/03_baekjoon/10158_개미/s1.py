# 가로, 세로
w, h = map(int, input().split())
# 좌표
x, y = map(int, input().split())
# 시간
t = int(input())

x_add = 1
y_add = 1

while t > 0:
    if x == w:
        x_add = -x_add
    elif x == 0:
        x_add = -x_add
    if y == 0:
        y_add = -y_add
    elif y == h:
        y_add = -y_add

    x += x_add
    y += y_add
    t -= 1
print(x, y)