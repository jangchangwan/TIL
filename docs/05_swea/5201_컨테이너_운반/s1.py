# 5201_컨테이너-운반_문제풀이
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    W_lst = list(map(int, input().split()))
    T_lst = list(map(int, input().split()))
    # 무거운 화물 순서대로 정렬하기
    W_lst.sort(reverse=True)
    # 적재용량이 큰 트럭 부터 정렬하기
    T_lst.sort(reverse=True)
    ans = 0
    # 큰것부터 비교해서 결과에 더해주기
    for t in range(M):
        w = 0
        while w < len(W_lst):
            # 담을 수 있는 경우
            if T_lst[t] >= W_lst[w]:
                ans += W_lst[w]
                # 화물 제거
                W_lst.pop(w)
                break
            w += 1

    print('#{} {}'.format(tc, ans))