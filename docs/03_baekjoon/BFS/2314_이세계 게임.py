"""
범위  4 X 4
상하좌우 스위칭
여러번 변경가능

before을 주고 after로 만들었을 경우 최소 횟수
불가능한 경우 주어지지 x
"""
from collections import deque

def BFS():
    q = deque()
    visited[before] = 0
    q.append(before)

    while len(q):
        cur = q.popleft()
        if cur == after:
            return visited[cur]

        for i in range(24):
            swap_a = 2 ** db[i][0]
            swap_b = 2 ** db[i][1]
            bit_a = cur & swap_a
            bit_b = cur & swap_b

            if bit_a == bit_b or bit_a * bit_b != 0:
                continue

            nxt = cur ^ swap_a ^ swap_b
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)   
    return -1
  
  
db = [
  (0, 1), (1, 2), (2, 3), (4, 5), (5, 6), (6, 7),
  (0, 4), (1, 5), (2, 6), (3, 7), (4, 8), (5, 9),
  (8, 9), (9, 10), (10, 11), (12, 13), (13, 14), (14, 15),
  (6, 10), (7, 11), (8, 12), (9, 13), (10, 14), (11, 15)
]


INF = 10 ** 5
visited = [-1] * 65536


before = ''
for _ in range(4):
    before += input()
before = before.replace('L', '0')
before = before.replace('P', '1')
before = int(before, 2)

input()

after = ''
for _ in range(4):
    after += input()
after = after.replace('L', '0')
after = after.replace('P', '1')
after = int(after, 2)

answer = BFS()
print(answer)