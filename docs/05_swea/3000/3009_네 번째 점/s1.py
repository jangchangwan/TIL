
x_list = []
y_list = []
result_x = 0
result_y = 0
# 입력 값 3개받아야함
for i in range(3):
    # x y 좌표를 받는다.
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)


for i in range(3):
    if x_list.count(x_list[i]) == 1:
        result_x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        result_y = y_list[i]
print('{} {}'.format(result_x, result_y))