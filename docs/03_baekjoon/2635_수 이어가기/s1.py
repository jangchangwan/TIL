
num = int(input())

# 결과 리스트 , 카운티 변수 설정
max_list = list()
max_cnt = 0
# 1부터 num-1 까지 반복
for i in range(1, num+1):
    cnt = 1
    cnt_list = [num, i]
    # 값이 양수일 경우 반복한다.
    while cnt_list[cnt] >= 0:
        data = cnt_list[cnt-1] - cnt_list[cnt]
        cnt_list.append(data)
        cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
        max_list = cnt_list

print(max_cnt)
for num in range(len(max_list)-1):
    if num == len(max_list)-2:
        print(max_list[num])
    else:
        print(max_list[num], end=' ')