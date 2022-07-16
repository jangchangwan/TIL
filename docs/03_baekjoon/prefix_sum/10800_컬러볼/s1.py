# 10800_컬러볼
# 2022-07-16
# 191200 KB / 880 ms

from collections import defaultdict

N = int(input())

# 인덱스순서대로 출력하기 위해서 인덱스 추가
ball = [[i] + list(map(int, input().split())) for i in range(N)]

# 크기순으로 정렬
ball.sort(key=lambda x: x[2])

answer = defaultdict(int)
temp = defaultdict(int)

total = 0  # 총합
idx = 0
for i in range(N):
    num, color, size = ball[i]
    while ball[idx][2] < size:  # 크기가 작을 때까지 수행
        total += ball[idx][2]
        temp[ball[idx][1]] += ball[idx][2]
        idx += 1
    answer[num] = total - temp[color]  # 총합 - 현재 색깔 공 누적합

for i in range(N):
    print(answer[i])