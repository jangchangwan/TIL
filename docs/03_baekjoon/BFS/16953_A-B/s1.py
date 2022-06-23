# 16953_A->B_문제풀이
# 2022-04-13

import sys
sys.stdin = open('input.txt', 'r')

'''
BFS 탐색으로 2배 와 1를 반복하여 탐색한다.
수가 초과되는경우 탐색을 멈춘다.
'''


def BFS(s):
    front = -1
    rear = 0
    queue = [s]
    visited[s] = 1
    while front != rear:
        temp = queue[front]
        print(temp)
        if temp == end:
            return visited[temp]

        elif temp > end:
            return

        for i in range(2):
            if i == 0:
                next_temp = temp * 2
            else:
                next_temp = temp * 10 + 1

            if next_temp <= end and visited[next_temp] == 0:
                queue.append(next_temp)
                visited[next_temp] = visited[temp] + 1
                rear += 1
    return



start, end = map(int, input().split())

visited = [0] * (end + 3)
ans = BFS(start)
print(ans)

