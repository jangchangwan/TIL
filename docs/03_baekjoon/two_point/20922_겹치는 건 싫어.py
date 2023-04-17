N, K = map(int, input().split())
N_list = list(map(int, input().split()))

left, right = 0, 0

counter = [0] * (max(N_list) + 1)
answer = 0
while right < N:
    if counter[N_list[right]] < K:
        counter[N_list[right]] += 1
        right += 1
    else:
        counter[N_list[left]] -= 1
        left += 1
    answer = max(answer, right - left)
    
print(answer)