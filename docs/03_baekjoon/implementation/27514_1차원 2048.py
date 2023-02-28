N = int(input())
N_list = list(map(int, input().split()))

# 날먹 실패
# check = list()

# for i in range(63):
#     check.append(2**i)

# SUM = sum(N_list)
# idx = 0
# while True:
#     if check[idx] < SUM:
#         idx += 1
#     else:
#         print(check[idx])
#         break
check = list()

for i in range(0, 63):
    check.append(2**i)

jisoo_list = [0] * 64

for num in N_list:
    if num == 0:
        continue
    for i in range(len(check)):
        if num == check[i]:
            jisoo_list[i] += 1
            break
result = 1

for i in range(63):
    if jisoo_list[i] > 0:
        temp  = jisoo_list[i] // 2
        jisoo_list[i+1] += temp
    
    if jisoo_list[i+1] > 0:
        result = max(result, 2**(i+1))
print(result)