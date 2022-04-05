import sys
sys.stdin = open('input.txt', 'r')

T = 5
for t in range(T):
    N, K = map(int, input().split())

    N_lst = list()
    K_lst = list()
    ans_list = list()
    # N 의 소인수분해
    for i in range(2, N):
        n = 2
        while n <= i:
            if i % n == 0:
                N_lst.append(n)
                i = i // n
            else:
                n += 1
    h = 2
    # K의 소인수분해
    while h <= K:
        if K % h == 0:
            K_lst.append(h)
            K = K // h
        else:
            h += 1

    j = 0
    result = 1
    # 공통된 소인수 찾아서 곱하기
    while j < len(K_lst):
        if K_lst[j] in N_lst:
            N_lst.remove(K_lst[j])
            result *= K_lst.pop(j)
        else:
            j += 1

    print(result)