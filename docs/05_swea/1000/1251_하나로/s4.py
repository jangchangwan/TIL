import sys
sys.stdin = open('input.txt', 'r')


def prim(n):
    D[n] = 0
    # G[n][n] = 0 <-- 없어도 된다. 이미 밖에서 자기 자신에게 도달하는 거리는 0 인것으로 초기화 되어있다. ex) G[0][0] = G[1][1] = G[2][2] ... = 0

    U = []
    for _ in range(N):
        mini = float("inf")
        for idx in range(N):
            if idx in U:
                continue
            if D[idx] < mini:
                mini = D[idx]
                key = idx
        U.append(key)

        for j in range(N):
            if j in U: continue
            # 이전에 풀었던 문제의 여파인가. 나도 모르게 조건을 G[key][j] + D[key] < D[j]으로 걸었다.
            # 이 문제에서 D[i]는 i번 섬에 부과되는 부담금이다. 그런데, 부과금이 부여되는 기준은 섬과 섬사이의 거리만으로 결정 되는것이고,
            # 이전 섬에 부여되었던 부과금은 하등 상관이 없기에  G[key][j]와 D[j] 만 비교하면 되는것이다
            if G[key][j] and G[key][j] < D[j]:  # + D[key] < D[j]:
                D[j] = G[key][j]  # + D[key]


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    # 그래프 생성 / 2차원으로 만들기
    G = [[0] * N for _ in range(N)]
    # 큰 output에 대해서 자꾸 삑이 나길래 뭐지 싶었는데, D에 넣은 적당히 큰 값보다 더 쎈 친구들이 와버렸다
    # 그래서 python에서 선언할수 있는 양의 무한대를 적었다
    D = [float("inf")] * N
    for i in range(N):
        for j in range(N):
            G[i][j] = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2  # 환경 부담금 구하기
            G[j][i] = G[i][j]

    prim(0)

    ans = 0
    for elem in D:
        ans += elem
    print('#{} {}'.format(tc, round(ans * E)))
