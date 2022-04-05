import sys
sys.stdin = open("input.txt")


def DFS(stack, r, c):
    global ans
    # 7자리 됬을 경우 set에 넣어주기
    if len(stack) == 7:
        ans.add(stack)
        return

    for d in delta:
        # 범위가 벗어난 경우 빠지기
        if r + d[0] < 0 or 4 <= r + d[0] or c + d[1] < 0 or 4 <= c + d[1]:
            continue
        # 동작
        DFS(stack + array[r + d[0]][c + d[1]], r + d[0], c + d[1])


T = int(input())
for t in range(1, T+1):
    array = [list(map(str, input().split())) for _ in range(4)]
    # 중복 제거
    ans = set()
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    # 완전탐색
    for i in range(4):
        for j in range(4):
            DFS(array[i][j], i, j)
    print("#{} {}".format(t, len(ans)))