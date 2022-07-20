# 1205 등수 구하기
# 2022-07-01

N, num, P = map(int, input().split())

if N:
    score = list(map(int, input().split()))
    score.append(num)
    score.sort(reverse=True)
    rank = score.index(num) + 1

    if rank > P:
        print(-1)
    else:
        if N == P and num == score[-1]:
            print(-1)
        else:
            print(rank)


else:
    print(1)