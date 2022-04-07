# 14891_톱니바퀴_문제풀이
# 2022-04-07

'''
12시가 맨처음 번호이므로 회전후 처음 번호를 확인하여 점수를 출력한다

조건 : 맞닿는 부분이 서로 다를경우
    옆 톱니바퀴가 움직이며 방향은 반대로 움직인다
    양옆에 톱니바퀴가 존재하므로 양쪽을 탐색해야한다.
    회전한후 리스트를 만들어 줘야한다.
'''
import sys
sys.stdin = open('input.txt', 'r')

def BFS(sn, sd):
    front = -1
    rear = 0
    queue = [(sn, sd)]
    visited[sn] = 1

    while front != rear:
        front += 1
        n, d = queue[front]
        # 좌우 탐색
        left = n - 1
        right = n + 1

        # 왼쪽에 톱니바퀴가 있을경우, 그 바퀴가 굴러 가는 경우
        if (0 < left < 5) and visited[left] == 0 and gears[n-1][6] != gears[left-1][2]:
            if d == 1:
                new_d = -1
            else:
                new_d = 1
            queue.append((left, new_d))
            visited[left] = 1
            rear += 1
        # 오른쪽 톱니바퀴인 경우
        if (0 < right < 5) and visited[right] == 0 and gears[n - 1][2] != gears[right - 1][6]:
            if d == 1:
                new_d = -1
            else:
                new_d = 1
            queue.append((left, new_d))
            visited[left] = 1
            rear += 1

        # 회전하기
        if d == 1:  # 시계 방향 회전, 값을 오른쪽으로 한칸씩 이동
            tmp = gears[n-1][7]
            for j in range(0, 8):
                gears[n-1][j], tmp = tmp, gears[n-1][j]

        else:  # 반시계 방향, 값을 왼쪽으로 한칸씩 이동
            tmp = gears[n-1][0]
            for j in range(7, -1, -1):
                gears[n-1][j], tmp = tmp, gears[n-1][j]


gears = [list(map(int, input())) for _ in range(4)]
T = int(input())


for tc in range(T):
    gear_num, dir = map(int, input().split())
    # 할때마다 초기화
    visited = [0] * 5
    BFS(gear_num, dir)

# 정답확인
ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += 2**i
print(ans)
