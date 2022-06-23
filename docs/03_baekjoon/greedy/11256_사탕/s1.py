# 11256_사탕
# 2022-06-22
# 그리드 + 정렬

T = int(input())

for tc in range(T):
    Candy, Box = map(int, input().split())
    Boxs = []
    for _ in range(Box):
        r, c = map(int, input().split())
        Boxs.append(r*c)

    Boxs.sort(reverse=True)

    cnt = 0
    while Candy > 0:
        Candy -= Boxs[cnt]
        cnt += 1
    print(cnt)