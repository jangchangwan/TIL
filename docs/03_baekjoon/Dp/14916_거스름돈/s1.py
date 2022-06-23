# 14916_거스름돈
# 2022-06-12

N = int(input())

ans = 0
# 5로 나누었을떄 홀수 일 경우
temp = N % 5
if N == 1 or N == 3:
    print(-1)
else:
    if temp % 2:
        ans += N // 5 + (temp + 5) // 2 - 1

    else:
        ans += N // 5 + temp // 2
    print(ans)