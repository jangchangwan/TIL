# 1232_사칙연산_문제풀이
# 2022-03-17
# 후위순회
def postorder(s):
    if s <= N:
        # 왼쪽 -> 오른쪽 -> 루트
        # 왼쪽
        if tree[s][1]:
            postorder(tree[s][1])
        # 오른쪽
        if tree[s][2]:
            postorder(tree[s][2])
        # 루트 (사칙연산)
        if tree[s][0] == '+':
            tree[s][0] = tree[tree[s][1]][0] + tree[tree[s][2]][0]
        elif tree[s][0] == '-':
            tree[s][0] = tree[tree[s][1]][0] - tree[tree[s][2]][0]
        elif tree[s][0] == '*':
            tree[s][0] = tree[tree[s][1]][0] * tree[tree[s][2]][0]
        elif tree[s][0] == '/':
            tree[s][0] = tree[tree[s][1]][0] / tree[tree[s][2]][0]


T = 10

for tc in range(1, T+1):
    # 노드 총 갯수
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]

    for i in range(N):
        node_info = input().split()
        # 노드가 4개인 경우
        if len(node_info) == 4:
            tree[int(node_info[0])][0] = node_info[1]   # 부모 노드
            tree[int(node_info[0])][1] = int(node_info[2])   # 왼쪽 자식 노드
            tree[int(node_info[0])][2] = int(node_info[3])   # 오른쪽 자식 노드
        # 하나인 경우
        else:
            tree[int(node_info[0])][0] = int(node_info[1])

    postorder(1)
    print('#{} {}'.format(tc, int(tree[1][0])))