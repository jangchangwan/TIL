# 10807_개수 세기
# 2022-06-05

# 간단한 배열 탐색 문제


N = int(input())
N_list = list(map(int, input().split()))
target = int(input())

# 1.for문으로 배열탐색
cnt = 0
for n in N_list:
    if n == target:
        cnt += 1

# 2. 내장함수 사용
cnt = N_list.count(target)

print(cnt)