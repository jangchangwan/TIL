# 25176_청정수열
# 2022-06-11

N = int(input())

res = 1
for n in range(1, N+1):
    res *= n
print(res)