def sosu(num):
    #num ~ 2num 까지 1인 배열을 만든다.
    sosu_arr = [0,0]+[1] * (num-1)

    for i in range(2,int(num**0.5)+1):
        if sosu_arr[i] == 1:
            j = 2

            while (i*j) <= num:
                sosu_arr[i*j] = 0
                j += 1
    return sosu_arr

while 1:
    number = int(input())
    if number == 0:
        break
    result = sosu(2*number)
    
    cnt = 0
    for i in range(number+1,2*number+1):
        if result[i] == 1:
            cnt += 1
    print(cnt)

