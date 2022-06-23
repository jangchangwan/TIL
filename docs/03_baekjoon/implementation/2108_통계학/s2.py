# 2108_통계학_문제풀이
# 2022-04-05
import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
N_lst = list(int(sys.stdin.readline()) for _ in range(N))


N_lst.sort()
# 평균값
print(round(sum(N_lst)/N))

# 중앙값
print(N_lst[N//2])

# 최빈값

cnt_lst = [0] * 4001
minus_cnt_lst = [0] * 4001
# 카운터 체크
for i in N_lst:
    if i >= 0:
        cnt_lst[i] += 1
    elif i < 0:
        minus_cnt_lst[-i] += 1
# 양수일 경우 최빈값 구하기 ( 0 포함 )
max_cnt = 0
res_cnt = []
for i in range(len(cnt_lst)):
    if cnt_lst[i] > max_cnt:
        res_cnt = []
        max_cnt = cnt_lst[i]
        res_cnt.append(i)
    elif cnt_lst[i] == max_cnt:
        res_cnt.append(i)
# 음수 일 경우 최빈 값 구하기 ( 0 미포함 )
max_minus_cnt = 0
res_minus_cnt = []
for i in range(len(minus_cnt_lst)):
    if minus_cnt_lst[i] > max_minus_cnt:
        res_minus_cnt = []
        max_minus_cnt = minus_cnt_lst[i]
        res_minus_cnt.append(-i)
    elif minus_cnt_lst[i] == max_minus_cnt:
        res_minus_cnt.append(-i)

# 최빈수에 따른 최빈값 합치기
if max_minus_cnt == max_cnt:
    res = res_cnt + res_minus_cnt
elif max_cnt > max_minus_cnt:
    res = res_cnt
else:
    res = res_minus_cnt

# 2개 이상일경우
if len(res) > 1:
    res.sort()
    print(res[1])
# 1개 일경우
elif len(res) == 1:
    print(res[0])
else:
    print(0)


# 최대값 - 최소값
print(N_lst[-1] - N_lst[0])