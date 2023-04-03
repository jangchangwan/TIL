# 입력
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())


# 방법 1 : 구현
# 초기화
# max_value = max(N_list)
# min_value = M // N
# sum_value = sum(N_list)
# # 국가에 재산이 지원요청금보다 많은 경우
# if sum_value <= M:
#     result = max_value
# # 국가에 재산이 지원요청금보다 적은 경우
# else:
#     while True:
#         temp = 0
#         for n in N_list:
#             if n <= min_value:
#                 temp += n
#             else:
#                 temp += min_value
        
#         if temp > M:
#             break
#         else:
#             result = min_value
#             min_value += 1


# 방법 2 : 이분 탐색
start, end = 0, max(N_list)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for n in N_list:
        if n > mid:
            total += mid
        else:
            total += n

    if total <= M:
        start = mid + 1
    else:
        end = mid - 1
    result = end
# 출력
print(result)