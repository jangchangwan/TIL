# 5202_화물_도크_문제풀이
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')


def DFS(node):
    global res
    if len(move[node]) == 0:
        res.append(len(visit))
        return
    else:
        if move[node]:
            for i in move[node]:
                visit.append(i)
                DFS(i)
                visit.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    print(N_arr)
    N_arr.sort()
    print(N_arr)
    total = 0
    # 딕셔너리 생성
    move = {}

    for i in range(N):
        move[i] = list()
        for j in range(N):
            # i의 끝 보다 j 의 스타트가 뒤에있는 경우
            if N_arr[j][0] >= N_arr[i][1]:
                move[i].append(j)

    res = []
    for k in range(N):
        visit = [k]
        DFS(k)
    print("#{} {}".format(tc, max(res)))
