N = int(input())

N_lst = []
for n in range(1,N+1):
    if N % n:
        continue
    N_lst.append(n)
print(*N_lst)