# 16235_나무제테크_문제풀이
# 2022-04-19


'''
나무는 봄마다 나이만큼 양분을 먹는다., 이 때 어린나무부터 먹인다.
처음 땅엔 모두 5인 양분을 가지고 시작한다.
죽은 나무는 나이의  2의몫만큼 양분이 된다.
번식하는 나무 조건 : 5의배수 and 인접한 8방향으로 나이가 1인 나무 생성
겨울에 A[r][c]만큼 양분을 추가해준다.

K 년후 나무 개수 출력
'''
import sys
sys.stdin = open('input.txt', 'r')


def grow():
    # 봄
    # 1. 어린나무부터 나무에게 양분주기
    # 2. 죽은나무를 양분으로 만들기
    global DDang, Trees

    add_tree = []
    remove_tree = []
    for i in range(N):
        for j in range(N):
            # 어린순으로 정렬
            Trees[i][j].sort()
            # 나무에게 양분주기
            temp = []
            for age in Trees[i][j]:
                if age <= DDang[i][j]:
                    DDang[i][j] -= age
                    age += 1
                    temp.append(age)
                    if age % 5 == 0:
                        add_tree.append((i, j))
                else:
                    remove_tree.append((i, j, age))
            Trees[i][j] = temp

    for i, j, age in remove_tree:
        DDang[i][j] += (age // 2)

    # 겨울
    # 1. 나무 번식
    # 2. 양분 추가
    # 새끼 나무 추가
    for r, c in add_tree:
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N):
                Trees[nr][nc].append(1)

    # 양분추가
    for i in range(N):
        for j in range(N):
            DDang[i][j] += arr[i][j]
    return


# 8 방향
dr = [-1, -1, -1, 1, 1, 1, 0, 0]
dc = [-1, 0, 1, -1, 0, 1, -1, 1]
# N : 땅 크기
# M : 초기 나무 갯수
# K : 경과 시간
N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

DDang = [[5] * N for _ in range(N)]

Trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, k = map(int, input().split())
    Trees[r-1][c-1].append(k)

for _ in range(K):
    grow()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(Trees[i][j])

print(answer)


# 메모리 218088 KB
# 시간 860 ms