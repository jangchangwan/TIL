def sosu(num):
    sosu_arr = [0,0]+[1] * (num-1)

    for i in range(2,int(num**0.5)+1):
        if sosu_arr[i] == 1:
            j = 2

            while (i*j) <= num:
                sosu_arr[i*j] = 0
                j += 1
    return sosu_arr

T = int(input())

for t in range(T):
    num = int(input())
    sosu_arr = sosu(num)
    # 소수 리스트를 만든다.
    half_a=num//2
    half_b=num//2
  
    for i in range(2,len(sosu_arr)):
        if sosu_arr[half_a] and sosu_arr[half_b]:
            print(half_a, half_b)
            break
        half_a -= 1
        half_b += 1