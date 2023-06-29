N, M = map(int, input().split())
    
distance = list(map(int, input().split()))
prefix_sum_distance = [0] * (N + 1)
prefix_sum_distance[1] = distance[0]
answer = 2000000000
for i in range(1, N+1):
    prefix_sum_distance[i] = prefix_sum_distance[i-1] + distance[i-1]


for _ in range(M):
    start, end, dis = map(int, input().split())
    if start > end:
        start, end = end, start
        
    if (end - start == 1):
        answer = min(answer, prefix_sum_distance[start] + dis + (prefix_sum_distance[N] - prefix_sum_distance[end]))
    
    answer = min(answer, prefix_sum_distance[start] + dis + (prefix_sum_distance[N] - prefix_sum_distance[end]) + (prefix_sum_distance[N] - prefix_sum_distance[start + 1]))
    answer = min(answer, dis * 2 + (prefix_sum_distance[N] - prefix_sum_distance[end]) * 2 + prefix_sum_distance[end - 1])
    answer = min(answer, prefix_sum_distance[end] + dis + prefix_sum_distance[N] - prefix_sum_distance[start])
    answer = min(answer, dis * 2 + prefix_sum_distance[N])
    
print(answer)