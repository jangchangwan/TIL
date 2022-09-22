# 1547_공
# 2022-07-10
# 구현


M = int(input())

balls = [0, 1, 0, 0]

for m in range(M):
    X, Y = map(int, input().split())
    balls[X], balls[Y] = balls[Y], balls[X]


for i in range(1, 4):
    if balls[i] == 1:
        print(i)