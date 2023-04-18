P, M = map(int, input().split())
data = [list(map(str, input().split())) for _ in range(P)]

# print(arr)
rooms = []

for level, id in data:
    flag = False
    level = int(level)
    
    
    for x, y in enumerate(rooms):
        if len(y) == M:
            continue
        if abs(y[0][0] - level) <= 10:
            rooms[x].append((level, id))
            flag = 1
            break
    if not flag:
        rooms.append([(level, id)])
# print(rooms)
for members in rooms:
        if len(members) == M:
            print('Started!')
        
        else:
            print('Waiting!')
        
        for level, name in sorted(members, key=lambda x: x[1]):
            print(level, name)

# # 방이 생성된 시간 순서로 출력
# for i in range(len(rooms)):
#     if len(rooms[i][1]) == m:
#         print('Started!')
#         tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
#         for j in range(m):
#             print(*tmp_ids[j])
#     else:
#         print('Waiting!')
#         tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
#         for j in range(len(tmp_ids)):
#             print(*tmp_ids[j])