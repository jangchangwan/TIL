# 5178_노드의_합_문제풀이
# 2022-03-18
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 노드, 리프노드, 노드번호
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        index, data = map(int, input().split())
        tree[index] = data

    # 역순 더 해줘야 한다
    for i in range(N, 0, -1):
        if tree[i] == 0:
            if i * 2 + 1 <= N:
                tree[i] = tree[i * 2] + tree[i * 2 + 1]
            else:
                tree[i] = tree[i * 2]

    print(tree)
    print('#{} {}'.format(tc, tree[L]))