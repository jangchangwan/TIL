import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
N_lst = list(map(int, input().split()))

max_sum = 0

for i in range(1 << N):
    temp = list()
    now_sum = 0
    for j in range(N):
        if i & (1 << j):
            temp.append(N_lst[j])
            now_sum += N_lst[j]
        # 3장을 넘어갈경우 빠져나온다
        if len(temp) > 3:
            temp = list()
            break
    # 3장이고 M보다 같거나 작을경우
    if len(temp) == 3 and now_sum <= M:
        # 최고점일경우 바로 빠져나오기
        if now_sum == M:
            max_sum = now_sum
            break
        elif now_sum > max_sum:
            max_sum = now_sum

print(max_sum)


