# 2559_수열_문제풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')


def my_max(lst):
    max_num = lst[0]
    for a in lst:
        if max_num < a:
            max_num = a
    return max_num


N, K = map(int, input().split())
num_list = list(map(int, input().split()))

now_sum = 0
# 더하는 과정을 한번만한다
for k in range(K):
    now_sum += num_list[k]
result = [now_sum]
# 차이값을 넣어준다
for i in range(N-K):
    now_sum = now_sum - num_list[i] + num_list[i+K]
    result.append(now_sum)
# 최대값 출력
print(my_max(result))
