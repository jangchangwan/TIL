# 1068_트리_문제풀이
# 2022-06-03

import sys
sys.stdin = open('input.txt', 'r')

'''
삭제되는 부분을 시작으로 자식들을 -2값으로 바꾸고
-2값이 아니거나 부모노드가 아닐경우 cnt를 증가시켜 값을 도출한다.
'''


def DFS(num, Tree):
    Tree[num] = -2
    for i in range(N):
        if num == Tree[i]:
            DFS(i, Tree)


N = int(input())
Tree = list(map(int, input().split()))
delete_Num = int(input())


DFS(delete_Num, Tree)
cnt = 0
for i in range(N):
    if Tree[i] != -2 and i not in Tree:
        cnt += 1

print(cnt)