import sys
sys.stdin = open('input.txt', 'r')

T = 5
for t in range(T):
    N, K = map(int, input().split())

    N_nums = 1
    K_lst = [K]
    ans_list = list()
    # N 의 소인수분해
    for i in range(2, N):
        N_nums *= i

    h = 2
    # K 의 소인수 찾기
    while h <= K:
        if K % h == 0:
            K_lst.append(K // h)
            K = K // h
        else:
            h += 1
    print(K_lst)
    for k in K_lst:
        if N_nums % k == 0:
            print(k)
            break
