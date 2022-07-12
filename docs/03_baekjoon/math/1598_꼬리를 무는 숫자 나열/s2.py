# 1598_꼬리를 무는 숫자 나열
# 2022-07-12
# 사칙
N, M = map(int, input().split())
N -= 1
M -= 1
print(abs(N // 4 - M // 4) + abs(N % 4 - M % 4))