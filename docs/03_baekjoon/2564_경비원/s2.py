import sys
sys.stdin = open('input.txt', 'r')


def trans_dis(point, location):
    global col, row
    # 북쪽
    if point == 1:
        return location
    # 남쪽
    elif point == 2:
        return col + row + col - location
    # 서쪽
    elif point == 3:
        return col + row + col + row - location
    # 동쪽
    else:
        return col + location


col, row = map(int, input().split())
# 총 길이
total_dir = (col + row)*2
N = int(input())
N_lst = list()
for n in range(N):
    dir, dis = map(int, input().split())
    N_lst.append(trans_dis(dir, dis))

s_dir, s_dis = map(int, input().split())
s_location = trans_dis(s_dir, s_dis)

res = 0
for n in N_lst:
    num_a = abs(s_location - n)
    num_b = (total_dir - abs(s_location - n))
    if num_a < num_b:
        res += num_a
    else:
        res += num_b
print(res)
