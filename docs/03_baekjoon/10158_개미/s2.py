# 가로, 세로
w, h = map(int, input().split())
# 좌표
x, y = map(int, input().split())
# 시간
t = int(input())
# w,h의 최소공배수가 될 경우 제자리로 되돌아온다
new_t = t % (w * h)
x_add = 1
y_add = 1

while new_t > 0:
    if x == w or x == 0:
        x_add = -x_add
    if y == 0 or y == h:
        y_add = -y_add
    x += x_add
    y += y_add
    new_t -= 1

print(x, y)