# 1327_소트게임_문제풀이
# 2022-06-03

import sys
sys.stdin = open('input.txt', 'r')


def BFS(word):
    global visited, res
    front = -1
    rear = 0
    queue = [(word, 0)]
    while front != rear:
        front += 1
        now, cnt = queue[front]
        now = list(now)

        if now == answer:
            res = cnt
            return
        for i in range(N-K+1):
            temp_now = now[:]
            temp = now[i:i+K]
            temp.reverse()
            for j in range(K):
                temp_now[i+j] = temp[j]
            temp_now = "".join(temp_now)
            if temp_now not in visited:
                visited.add(temp_now)
                queue.append((temp_now, cnt+1))
                rear += 1

N, K = map(int, input().split())
N_lst = list(map(str, input().split()))
word = ''.join(N_lst)
visited = set(word)
answer = sorted(word)
res = -1
BFS(word)
print(res)