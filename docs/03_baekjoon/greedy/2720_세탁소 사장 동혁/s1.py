# 2720_세탁소 사장 동혁_문제풀이
# 2022-04-29

# 간단한 그리디 알고리즘

T = int(input())

for _ in range(T):
    N = int(input())
    change = [25, 10, 5, 1]
    ans = [0] * 4

    for i in range(4):
        ans[i] = N // change[i]
        N %= change[i]

    print(*ans)