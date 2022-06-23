# 1969_DNA
# 2022-06-22

N, M = map(int, input().split())
N_lst = [input() for _ in range(N)]

answer = ''
cnt = 0

for i in range(M):
    A, C, G, T = 0, 0, 0, 0
    for j in range(N):
        if N_lst[j][i] == 'A':
            A += 1
        elif N_lst[j][i] == 'C':
            C += 1
        elif N_lst[j][i] == 'G':
            G += 1
        elif N_lst[j][i] == 'T':
            T += 1

    if max(A, C, G, T) == A:
        answer += 'A'
        cnt += C + G + T
    elif max(A, C, G, T) == C:
        answer += 'C'
        cnt += A + G + T
    elif max(A, C, G, T) == G:
        answer += 'G'
        cnt += A + C + T
    elif max(A, C, G, T) == T:
        answer += 'T'
        cnt += A + C + G

print(answer)
print(cnt)