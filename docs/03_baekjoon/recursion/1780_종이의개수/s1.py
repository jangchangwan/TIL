# 1780_종이의개수_문제풀이
# 2022-03-30

import sys
sys.stdin = open('input.txt', 'r')


# 모두 같은 수인지 체크하는 함수
def check(x, y, n):
    val = matrix[x][y]
    for i in range(n):
        for j in range(n):
            # 모두 같은 수가 아님
            if val != matrix[x+i][y+j]:
                return False
    return True


def divide(x, y, n):
    # 모두 같은 수일 때
    if check(x, y, n):
        # 매트릭스 값은 -1,0,1 Result 인덱스는 0,1,2이므로 1을 더해준다
        result[matrix[x][y] + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(x + i * n // 3, y + j * n // 3, n // 3)


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = [0] * 3

divide(0, 0, n)
for i in range(3):
    print(result[i])