# 2467_용액_문제풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt', 'r')

'''
정렬된 상태로 데이터를 준다
산성와 알칼리성가 둘다있을경우 같은부호끼리는 계산할 필요가없다
하지만 한쪽만 존재하는경우가있기에
양끝에서 시작해서 값이 0 보다 클경우 특성값이 큰값을 줄이고
0보다 작을경우 특성값이 작은 값을 줄여서 값을 찾아보자
'''
input = sys.stdin.readline
# 입력
N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()
min_ans = 20000000000
start, end = 0, (N-1)
ans = [0, 1]
while start < end:
    temp = N_lst[start] + N_lst[end]

    # 0 일경우
    if temp == 0:
        ans[0] = start
        ans[1] = end
        break
    elif abs(temp) < min_ans:
        ans[0] = start
        ans[1] = end
        min_ans = abs(temp)

    if temp > 0:
        end -= 1
    else:
        start += 1


print(N_lst[ans[0]], N_lst[ans[1]])