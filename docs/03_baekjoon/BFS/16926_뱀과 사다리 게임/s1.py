# 16926_뱀과 사다리 게임_문제풀이
# 2022-05-15

import sys
sys.stdin = open('input.txt', 'r')


def BFS():
    queue = [1]
    front = -1
    rear = 0
    visited_ladder[1] = 1
    while front != rear:
        front += 1
        now = queue[front]
        # 종료조건
        if now == 100:
            return
        for move in range(1, 7):
            move_now = now + move
            if (0 < move_now <= 100) and (visited_ladder[move_now] == 0):
                # 사다리 & 뱀 통과
                if move_now in ladder_dic.keys():
                    move_now = ladder_dic[move_now]
                # 재검사
                if visited_ladder[move_now] == 0:
                    queue.append(move_now)
                    rear += 1
                    visited_ladder[move_now] = visited_ladder[now] + 1


# 입력
ladder, snake = map(int, input().split())
ladder_dic = {}
for _ in range(ladder+snake):
    start, end = map(int, input().split())
    ladder_dic[start] = end
visited_ladder = [0] * 101

BFS()
print(visited_ladder[100]-1)