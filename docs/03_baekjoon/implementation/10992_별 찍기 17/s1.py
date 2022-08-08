# 10992 별 찍기 17
# 2022-08-08

N = int(input())
print(" "*(N-1) + "*")
if(N!=1):
    for i in range(1,N-1):
        print(" " * (N-1-i) + "*" + " " * (2*i-1) + "*")
    print("*" * (2*N-1))