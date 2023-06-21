"""
pizza
"""

N = int(input())
pizza_list = list(map(int, input().split()))


sum_value = sum(pizza_list)

answer_list = [0] * N
time = 0
idx = 0

# 전체 값 0이 되면 종료
while sum_value:
    
    # 더이상 피자가 필요없는사람은 무시 
    if pizza_list[idx] == 0:
        idx += 1
        if idx == N:
            idx = 0
        continue

    sum_value -= 1
    pizza_list[idx] -= 1
    time += 1
    # 피자를 받고 0이 되는 경우 저장 
    if pizza_list[idx] == 0:
        answer_list[idx] = time
    
    idx += 1
    if idx == N:
        idx = 0
print(*answer_list)