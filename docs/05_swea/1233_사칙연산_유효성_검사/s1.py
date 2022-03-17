# 1233_사칙연산_유효성_검사_문제풀이
# 2022-03-17
import sys
sys.stdin = open('input.txt', 'r')


# 중위순회
def in_order(T):
    if T <= N:
        in_order(T*2)
        ans.append(tree[T])
        in_order(T * 2 + 1)
    return


T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    ans = []
    for n in range(1, N+1):
        temp = list(input().split())
        tree[n] = temp[1]
    in_order(1)
    result = 1
    for i in range(N):
        if i % 2:
            if ans[i] in ['+', '-', '*', '/']:
                continue
            else:
                result = 0
                break
        else:
            if ans[i].isdigit():
                continue
            else:
                result = 0
                break
    print(ans)
    print('#{} {}'.format(tc, result))