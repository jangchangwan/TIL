# 20310_타노스
# 2022-06-22


N = input()

zero_cnt = 0
one_cnt = 0
for n in N:
    if n == '0':
        zero_cnt += 1
    else:
        one_cnt += 1

remove_zero = zero_cnt // 2
remove_one = one_cnt // 2

start = 0
end = len(N)-1
answer = ''
idx = []

while (remove_zero != 0) or (remove_one != 0):
    if N[start] == '1' and remove_one > 0:
        remove_one -= 1
        idx.append(start)

    if N[end] == '0' and remove_zero > 0:
        remove_zero -= 1
        idx.append(end)

    start += 1
    end -= 1

for i in range(len(N)):
    if i in idx:
        continue
    answer += N[i]
print(answer)