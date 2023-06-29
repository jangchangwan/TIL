E, L, B = map(int, input().split())

distance = [0] * (E + 1)

for _ in range(B):
    cow = int(input())
    distance[cow] = 1

count = 0
now = 0
power = L
while now != E:
    # 소가 있는 경우
    now += power
    if now > E or distance[now]:
        now -= power
        power -= 1
    # 소가 없는 경우
    else:
        power = L
        count += 1    
    # 건너갈수 없는 경우
    if power == 0:
       count = -1
       break

print(count)
