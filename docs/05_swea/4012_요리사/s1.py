import sys
sys.stdin = open('input.txt', 'r')


# 최소값 구하기
def my_min(arr_1, arr_2):
    global ans
    sum_1 = sum_2 = 0
    for i in range(M):
        for j in range(M):
            if arr_1[i] != arr_1[j]:
                sum_1 += (N_lst[arr_1[i]][arr_1[j]])
            if arr_2[i] != arr_2[j]:
                sum_2 += (N_lst[arr_2[i]][arr_2[j]])
    ans = min(ans, abs(sum_1-sum_2))
    print(ans)
    print(arr_1, arr_2)

# 조합 만들기
def comb_dfs(s):
    if len(stack) == M:
        ans_lst.append(stack[:])

    else:
        for i in range(s, N):
            visited[i] = 1
            stack.append(i)
            comb_dfs(i+1)
            visited[i] = 0
            stack.pop()


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    N_lst = [list(map(int, input().split())) for _ in range(N)]
    M = N // 2

    ans_lst = []
    stack = []
    visited = [0] * N
    comb_dfs(0)
    ans = 999999
    print(len(ans_lst))
    for i in ans_lst:
        # 나머지 리스트
        not_ans_lst = []
        for j in range(N):
            if j not in i:
                not_ans_lst.append(j)
        my_min(i, not_ans_lst)


    print('#{} {}'.format(tc, ans))