# 요세푸스 문제0_문제풀이
# 2022-04-07

# 원형큐 문제
# 일반적인 BFS 문제로 풀었다
import sys
sys.stdin = open('input.txt', 'r')


def BFS():
    global res
    front = -1
    rear = N-1
    queue = N_lst
    cnt = 1
    while front != rear:

        front += 1
        temp = queue[front]
        # M 단계마다 res에 넣어주기
        if cnt % M == 0:
            res.append(temp)
        # 아닐경우
        else:
            queue.append(temp)
            rear += 1
        cnt += 1

    return

N, M = map(int, input().split())

N_lst = [i for i in range(1, N+1)]
res = []
BFS()
print('<', end='')
for i in range(len(res)):
    if i == N-1:
        print(res[i], end='')
    else:
        print(res[i], end=', ')
print('>')