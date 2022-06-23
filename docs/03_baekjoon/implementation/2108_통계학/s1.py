# 2108_통계학_문제풀이
# 2022-04-05
import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
N_lst = list(int(sys.stdin.readline()) for _ in range(N))


N_lst.sort()
# 평균값
print(round(sum(N_lst)//N))
# 중앙값
print(N_lst[N//2])
# 최빈값

max_number = []
max_cnt = 0
for i in N_lst:
    if max_cnt == N_lst.count(i):
        max_number.append(i)
    elif max_cnt < N_lst.count(i):
        # 초기화
        max_number = []
        max_number.append(i)
        max_cnt = N_lst.count(i)

# 2개 이상일경우
if len(max_number) > 1:
    max_number.sort()
    print(max_number[1])
# 1개 일경우
elif len(max_number) == 1:
    print(max_number[0])
else:
    print(0)
# 최대값 - 최소값
print(N_lst[-1] - N_lst[0])