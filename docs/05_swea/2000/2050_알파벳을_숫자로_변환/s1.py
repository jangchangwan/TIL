print(ord('B')-64)
A_lst = input()
N_lst = []
for a in A_lst:
    N_lst.append(ord(a)-64)

print(*N_lst)