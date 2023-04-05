# 입력
N, X = map(int, input().split())
blogs = list(map(int, input().split()))

# 초기화
# count = 0

# 방법 1 : 구현
# for i in range(N-X+1):
#     value = sum(blogs[i:i+X])
#     print(value)
#     # 최대 방문자가 많을 경우
#     if value > max_value:
#         max_value = value
#         count = 1
#     # 같을 경우
#     elif value == max_value:
#         count += 1
#     # 적을 경우
#     else:
#         pass
    
# 방법 2 : 투포인터

if max(blogs) == 0:
    print("SAD")
else:
    value = sum(blogs[:X])
    count = 1
    max_value = value
    for i in range(1, N-X+1):
        value = value - blogs[i-1] + blogs[i+X-1]   
        # 최대 방문자가 많을 경우
        if value > max_value:
            max_value = value
            count = 1
        # 같을 경우
        elif value == max_value:
            count += 1
        # 적을 경우
        else:
            pass

    # 출력
    print(max_value)
    print(count)
    