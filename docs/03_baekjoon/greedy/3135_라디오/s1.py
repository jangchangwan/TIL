# 3135_라디오
# 2022-06-29

# 입력
start, end = map(int, input().split())
N = int(input())
N_lst = [int(input()) for _ in range(N)]

answer = 0
if end in N_lst:
    answer = 1
else:
    answer = abs(start - end)
    for n in N_lst:
        answer = min(answer, abs(end - n)+1)
print(answer)
