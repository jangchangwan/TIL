import sys
sys.stdin=open("input.txt", 'r')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 1~12를 담고 있는 집합 arr
    arr = list(range(1, 13))
    cnt = 0
    # 부분집합 생성
    for i in range(1 << 12): # 공집합을 제외한  모든 부분집합 검사
        sublist = []
        sum_arr = 0
        for j in range(12): # arr 의 모든 원소 루프
            # & : 비트연산자로 2진수가 두값이 동일할경우 True 아닐경우 False로 반환
            # i 의 j 번째 비트가 1이면 j번째 원소 출력
            if i & (1 << j):
                sublist.append(arr[j])
                sum_arr += arr[j]
        # print(sublist)
        # 개수가 N 이 맞고 합이 K일 경우
        if len(sublist) == N and sum_arr == K:
            cnt += 1
        # 합이 너무커질경우 바로 빠져나온다!
        if sum_arr > K*1.5:
            break

    ans = cnt
    print('#{} {}'.format(tc, ans))