# 1092_배_문제풀이
# 2022-06-08

'''
박스를 배로 옮길 수 없는 경우 -1 출력 => cranes < boxes
모든 박수를 배로 옮기는데 드는 최소 시간
'''

# 입력
N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 변수설정
time = 0
visited = [0 for _ in range(M)]
count = 0  # 옮긴 박스의 개수

positions = [0] * N

if boxes[0] > cranes[0]:
    print(-1)
else:
    while count < len(boxes):
        for i in range(N):  # 크레인에 대하여
            while positions[i] < len(boxes):
                # 아직 안 옮긴 박스 중에서, 옮길 수 있는 박스를 만날 때까지 반복
                if not visited[positions[i]] and cranes[i] >= boxes[positions[i]]:
                    visited[positions[i]] = 1
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        time += 1
    # 출력
    print(time)
