# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.


def sosu(num):
    sosu_arr = [0,0]+[1] * (num-1)

    for i in range(2,num+1):
        if sosu_arr[i] == 1:
            j = 2

            while (i*j) <= num:
                sosu_arr[i*j] = 0
                j += 1
    return sosu_arr
                
first_num,final_num = map(int,input().split())

result = sosu(final_num)
for i in range(first_num,len(result)):
    if result[i] == 1:
        print(i)