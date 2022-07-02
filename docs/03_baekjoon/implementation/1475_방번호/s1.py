# 1475_방번호
# 2022-07-02
# 구현
# 체크리스트를 만들어 번호별 체크횟수를 보고 최대값 추출
N = input()

check = [0] * 9

for n in N:
    num = int(n)
    if num == 9:
        check[6] += 1
    else:
        check[num] += 1

max_cnt = 0

for i in range(9):
    if i == 6:
        if check[i] % 2:
            max_cnt = max(max_cnt, (check[i] // 2) + 1)
        else:
            max_cnt = max(max_cnt, check[i] // 2)
    else:
        max_cnt = max(max_cnt, check[i])


print(max_cnt)