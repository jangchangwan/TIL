bridge = int(input()) # 굴다리의 길이
lamp = int(input()) # 가로등의 개수
lamps = list(map(int, input().split()))# 가로등 위치

answer = 0

if len(lamps) == 1:
    answer = max(lamps[0] - 0, bridge - lamps[0])
    
else:
    for i in range(len(lamps)):
        if i == 0:
            height = lamps[i] - 0
        elif i == len(lamps) - 1:
            height = bridge - lamps[i]
        else:
            tmp = lamps[i] - lamps[i-1]
            if tmp % 2:
                height = tmp // 2 + 1
            else:
                height = tmp // 2
        answer = max(height, answer)

print(answer)