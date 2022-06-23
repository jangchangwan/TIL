# 1966_프린트-큐-문제풀이
# 2022-03-27
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 문서 수
    N, M = map(int, input().split())

    queue = list(map(int, input().split()))

    front = -1
    rear = len(queue)

    cnt = 0
    while front != rear:
        max_num = max(queue[front:rear])
        front += 1
        temp = queue[front]
        # 중요도가 가장 클경우
        if temp == M:
            cnt += 1
            if M == 0:  # 원하는 문서인 경우 프린트
                print(cnt)
                break
            else:
                M -= 1

        else:
            queue.append(temp)
            rear += 1
            if M == 0:
                M = N - cnt - 1
            else:
                M -= 1
