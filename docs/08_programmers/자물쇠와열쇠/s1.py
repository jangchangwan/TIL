# 자물쇠와 열쇠_문제풀이
# 2022-04-25

def rotate90(arr):
    return list(zip(*arr[::-1]))


def check(arr, N, M):
    for i in range(N):
        for j in range(N):
            if arr[M + i][M + j] != 1:
                return False
    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)

    arr = [[0] * (M*2+ N) for _ in range(M*2 + N)]

    # Lock 중앙 배치
    for i in range(N):
        for j in range(N):
            arr[M + i][M + j] = lock[i][j]

    for _ in range(4):
        key = rotate90(key)
        for i in range(1, M+N):
            for j in range(1, M+N):
                # 키 넣어보기
                for r in range(M):
                    for c in range(M):
                        arr[i+r][j+c] += key[r][c]

                # 확인
                if check(arr, M, N):
                    return True
                # 키 빼기
                for r in range(M):
                    for c in range(M):
                        arr[i+r][j+c] -= key[r][c]

    return False






key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))