N = int(input())
N_lst = list(map(int, input().split()))

N_lst.sort()
print(N_lst[N//2])