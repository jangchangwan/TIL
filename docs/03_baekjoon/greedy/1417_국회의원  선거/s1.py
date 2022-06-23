# 1417_국회의원 선거
# 2022-06-11

N = int(input())
N_lst = list(int(input()) for _ in range(N))


if N == 1:
    print(0)

else:
    me = N_lst[0]
    other = N_lst[1:]
    other.sort()
    ans = 0
    while other[-1] >= me:
        me += 1
        other[-1] -= 1
        ans += 1
        other.sort()
    print(ans)