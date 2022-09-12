# 1673_치킨 쿠폰
# 2022-09-08


while True:
    try:
        N, K = map(int, input().split())
        answer = N
        while N // K:
            answer += N // K
            N = N // K + N % K
        print(answer)
    except:
        break