# 12852_1로 만들기 2_문제풀이
# 2022-05-27

from collections import deque

X = int(input())
q = deque()
q.append([X])

ans = []
while q:
    temp = q.popleft()
    x = temp[0]

    if x == 1:
        ans = temp
        break

    if x % 3 == 0:
        q.append([x // 3] + temp)

    if x % 2 == 0:
        q.append([x // 2] + temp)

    q.append([x - 1] + temp)


print(len(ans) - 1)
print(*ans[::-1])