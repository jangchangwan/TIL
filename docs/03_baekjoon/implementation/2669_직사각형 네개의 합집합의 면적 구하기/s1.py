import sys
sys.stdin = open('input.txt', 'r')

# 101 x 101 행렬 생성
arr = [[0]*101 for _ in range(101)]
# 입력 총 4번
T = 4
min_x = min_y = 100
max_x = max_y = 0
for t in range(T):
    # 데이터 받기
    x1, y1, x2, y2 = map(int, input().split())

    # 범위 안에 있을 경우 1로 변경
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

result = 0
for row in arr:
    for i in range(len(row)):
        result += row[i]

print(result)




