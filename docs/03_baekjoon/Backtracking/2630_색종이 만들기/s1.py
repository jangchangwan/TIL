# 2630_색종이 만들기
# 2022-07-05


def back_tracking(r, c, size):
    global white, blue

    color = arr[r][c]
    for i in range(r, r+size):
        for j in range(c, c+size):
            if color != arr[i][j]:
                # 분할탐색
                back_tracking(r, c, size // 2)
                back_tracking(r + size // 2, c, size // 2)
                back_tracking(r, c + size // 2, size // 2)
                back_tracking(r + size // 2, c + size // 2, size // 2)
                return

    # 모든 컬러가 white 인경우
    if color == 0:
        white += 1
        return
    # 모든 경우가 blue 인 경우
    else:
        blue += 1
        return


# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

# 탐색
back_tracking(0, 0, N)

# 출력
print(white)
print(blue)