# 11659_구간합구하기

import sys
sys.stdin = open('input.txt', 'r')


'''

누적합은 말 그대로 구간의 누적합을 구하는 문제입니다.
일반적으로  사용되는 배열에 값을 저장하고 지정된 인덱스부터 하나씩 더해가는 방식은 
최악의 경우O(n^2)의 시간복잡도를 갖기 때문에 입력의범위가 클 때 사용할 수 없습니다.
하지만 Prefix sum 방식을 사용하면 O(N)으로 해결 할 수 있습니다.
누적합은 문제에서 수열이 주어지고 어떤 구간의 값의 합을 구해야 할 때 쓰일 수 있습니다. 

'''
input = sys.stdin.readline


N, M = map(int, input().split())

N_lst = list(map(int, input().split()))
N_sum = [0 for _ in range(N)]
N_sum[0] = N_lst[0]

for i in range(1, N):
    N_sum[i] = N_sum[i-1] + N_lst[i]

# print(N_lst)
# print(N_sum)
for _ in range(M):
    start, end = map(int, input().split())
    ans = N_sum[end-1] - N_sum[start-1] + N_lst[start-1]
    print(ans)