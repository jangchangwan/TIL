
while True:
    # 세 변의 길이 받아오기
    num_list = list(map(int, input().split()))
    # 버블 정렬하기
    if num_list[0] == 0 and num_list[1] == 0 and num_list[2] == 0:
        break
    for i in range(2, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    if num_list[0]**2+num_list[1]**2 == num_list[2]**2:
        print('right')
    else:
        print('wrong')