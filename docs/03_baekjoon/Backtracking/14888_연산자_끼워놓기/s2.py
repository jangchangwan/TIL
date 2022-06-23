# 14888_연산자_끼워놓기_문제풀이
# 2022-04-01
# DFS로 풀자


import sys
sys.stdin = open('input.txt', 'r')


def DFS(i, ans):

    global max_ans, min_ans
    # 종료조건
    if i == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
    else:
        # 더하기
        if oper_lst[0] > 0:
            oper_lst[0] -= 1
            DFS(i+1, ans + num_lst[i])
            oper_lst[0] += 1
        # 빼기
        if oper_lst[1] > 0:
            oper_lst[1] -= 1
            DFS(i+1, ans - num_lst[i])
            oper_lst[1] += 1
        # 곱하기
        if oper_lst[2] > 0:
            oper_lst[2] -= 1
            DFS(i+1, ans * num_lst[i])
            oper_lst[2] += 1
        # 나누기
        if oper_lst[3] > 0:
            oper_lst[3] -= 1
            if ans < 0:
                DFS(i+1, -(abs(ans) // num_lst[i]))
            else:
                DFS(i+1, ans // num_lst[i])
            oper_lst[3] += 1


N = int(input())

num_lst = list(map(int, input().split()))
oper_lst = list(map(int, input().split()))

max_ans = -1000000000
min_ans = 1000000000

DFS(1, num_lst[0])
print(max_ans)
print(min_ans)