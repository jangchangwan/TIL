# 15686_치킨배달_문제풀이
# 2022-04-11

'''
집과 치킨집의 좌표를 뽑아낸다음
살릴 치킨집은 조합 알고리즘으록 구해서
문제에서 제시한것처럼 빼주기만하자..

'''
import sys
sys.stdin = open('input.txt', 'r')


# 조합 만들기
def chicken_order(n, picked, toPick):
    global orders
    if toPick == 0:
        orders.append(picked[:])
        return

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            chicken_order(n, picked, toPick - 1)
            picked.pop()


# N : 행렬의 크기
# M : 치킨집 수
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


house = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))
            arr[i][j] = 0

# 순서뽑기
orders = []
chicken_order(len(chicken), [], M)

min_cnt = 987654321
# 조합만큼 반복
for order in orders:

    cnt = 0
    for h in house:
        temp = 987654321
        for i in range(M):
            temp = min(temp, abs(chicken[order[i]][0] - h[0]) + abs(chicken[order[i]][1] - h[1]))
        cnt += temp
    min_cnt = min(min_cnt, cnt)

print(min_cnt)