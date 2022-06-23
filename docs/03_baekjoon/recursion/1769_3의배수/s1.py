# 1769_3의 배수
# 2022-06-20

def conversion(string, cnt):
    if len(string) > 1:
        cnt += 1
        n = 0
        for i in string:
            n += int(i)
        conversion(str(n), cnt)
    else:
        if int(string) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")


N = input()
cnt = 0
conversion(N, cnt)