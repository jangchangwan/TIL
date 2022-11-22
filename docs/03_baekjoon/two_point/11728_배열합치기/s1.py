M,N = map(int, input().split())

M_list = list(map(int, input().split()))
N_list = list(map(int, input().split()))

i, j = 0, 0
idx = 0
result = [0] * (M + N)

while idx < (M+N):
    if (i >= M):
        result[idx] = N_list[j]
        idx += 1
        j += 1
    elif (j >= N):
        result[idx] = M_list[i]
        idx += 1
        i += 1
    else:
        if (M_list[i] < N_list[j]):
            result[idx] = M_list[i]
            idx += 1
            i += 1
        else:
            result[idx] = N_list[j]
            idx += 1
            j += 1

print(*result)