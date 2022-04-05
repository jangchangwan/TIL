# 5189_전자카드_문제풀이
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')


def cart_order(n, picked, toPick):
    if toPick == 0:
        # 다시 돌아와야하므로 초기위치인 1을 더해준다
        temp = picked[:] + [1]
        temp_lst.append(temp)
        return

    for i in range(2, n+1):
        # 중복을 제외하기위해서 같은 숫자가 있을 경우 동작하지않는다.
        if i in picked:
            continue
        picked.append(i)
        cart_order(n, picked, toPick - 1)
        picked.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    temp_lst = []
    cart_order(N, [1], N-1)
    min_ans = 999999
    for i in temp_lst:
        ans = 0
        # 순서에 따른 값 구해주기
        for j in range(N):
            ans += N_arr[i[j]-1][i[j+1]-1]
        # 최소값 비교
        if ans < min_ans:
            min_ans = ans
    # 출력
    print('#{} {}'.format(tc, min_ans))



