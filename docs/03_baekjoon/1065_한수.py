number = int(input())

def hansu (number):
    # 한수의 갯수 카운팅
    cnt = 0
    # 1~99까지 모든수는 한수이기 때문에
    if number < 100 :
        cnt = number
        return cnt
    
    else :
        for num in range(100,number+1):
            if int(str(num)[0])-int(str(num)[1]) == int(str(num)[1])-int(str(num)[2]):
                cnt += 1
        return cnt+99

print(hansu(number))