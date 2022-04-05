# 5177_이진힙_문제풀이
# 2022-03-17
import sys
sys.stdin = open('input.txt', 'r')


# 노드 변환
def change_node(child):
    parent = child // 2
    # 부모 노드값이 더 클 경우
    if tree[parent] > tree[child]:
        # 스위칭
        tree[parent], tree[child] = tree[child], tree[parent]
        # 부모 노드도 확인하기
        change_node(parent)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))
    tree = [0] * (N + 1)
    for i in range(1, len(N_lst) + 1):
        tree[i] = N_lst[i-1]
        # 처음에 동작 X
        if len(tree) == 1:
            continue
        change_node(i)
    # 조상노드 모두 구하기
    last_node = N
    sum_node = 0
    while last_node > 1:
        last_node //= 2
        sum_node += tree[last_node]

    print('#{} {}'.format(tc, sum_node))
