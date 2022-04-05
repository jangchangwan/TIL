# 2105_디저트카페_문제풀이
# 2022-03-22

import sys
sys.stdin = open('input.txt', 'r')


def my_func():
    # 역순으로
    for length in range(N - 1, 1, -1):
        # 0 제외시키기
        for i in range(1, length):
            j = length - i
            for r in range(i, N - j):
                for c in range(N - i - j):

                    dessert_arr = [False] * 101
                    y, x = r, c

                    for d in range(4):
                        n = j if d % 2 else i
                        for _ in range(n):
                            y, x = y + dy[d], x + dx[d]
                            # 중복 체크
                            if not dessert_arr[arr[y][x]]:
                                dessert_arr[arr[y][x]] = True
                            # 중복일 경우 빠져나오기
                            else:
                                break
                        else:
                            continue
                        break
                    else:
                        return length * 2

    return -1


T = int(input())

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = my_func()

    print('#{} {}'.format(tc, ans))