# 14655_욱제는 도박쟁이야
# 2022-06-11

N = int(input())

round_1 = list(map(int, input().split()))
round_2 = list(map(int, input().split()))

ans = 0
for n in range(N):
    ans += abs(round_1[n]) + abs(round_2[n])

print(ans)
